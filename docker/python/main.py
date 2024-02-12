from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import json
import mysql.connector

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get':
            response = self.get_iterator_status()
        elif self.path == '/health':
            response = self.health_status()
        else:
            super().do_GET()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))

    def do_POST(self):
        if self.path == '/add':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            response = self.add_iterator(json.loads(post_data.decode('utf-8')))
        else:
            super().do_POST()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))

    def health_status(self):
        return json.dumps({'status': 'OK'})

    def get_iterator_status(self):
        db_connection = mysql.connector.connect(user='root', password='root', host='172.10.0.10', database='iterator-db')
        cursor = db_connection.cursor()

        try:
            cursor.execute("SELECT state FROM interator")
            state = cursor.fetchone()[0]
            return json.dumps({'status': 'OK', 'iterator': state})
        except Exception as e:
            return json.dumps({'status': 'Error', 'message': str(e)})
        finally:
            cursor.close()
            db_connection.close()

    def add_iterator(self, data):
        try:
            value = int(data.get('value'))
        except (ValueError, TypeError):
            return json.dumps({'status': 'Error', 'message': 'Invalid input'})

        db_connection = mysql.connector.connect(user='root', password='root', host='172.10.0.10', database='iterator-db')
        cursor = db_connection.cursor()

        try:
            cursor.execute("UPDATE iterator SET state = %s", (value,))
            db_connection.commit()
            return json.dumps({'status': 'OK', 'message': 'Iterator value updated successfully'})
        except Exception as e:
            return json.dumps({'status': 'Error', 'message': str(e)})
        finally:
            cursor.close()
            db_connection.close()

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = TCPServer(server_address, MyHandler)

    print('Serveur démarré sur le port 8080...')
    httpd.serve_forever()
