from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import json
import mysql.connector

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get':
             self.get_iterator_status()
        elif self.path == '/health':
            self.send_json_response(200, {"status": "OK"})
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/add':
            self.add_iterator()
        else:
            self.send_error(404)

    def get_iterator_status(self):
        try:
            with self.get_db_connection() as cnx:
                cursor = cnx.cursor()
                query = ("SELECT * FROM interator")
                cursor.execute(query)
                iterators = [{"state": state} for state in cursor]
                self.send_json_response(200, {"status": "ok", "iterators": iterators})
        except Exception as e:
            self.send_json_response(404, {'status': 'Error', 'message': str(e)})
        finally:
            cursor.close()

    def add_iterator(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            value = data['value']
            with self.get_db_connection() as cnx:
                cursor = cnx.cursor()
                query = ("INSERT INTO interator (state) VALUES (%s)")
                cursor.execute(query, (value,))
                cnx.commit()
                self.send_json_response(200, {"status": "ok", "message": "Iterator value added successfully"})
        except Exception as e:
            self.send_json_response(404, {'status': 'Error', 'message': str(e)})
        finally:
            cursor.close()

    def get_db_connection(self):
            return mysql.connector.connect(user='root', password='root', host='172.10.0.10', database='iterator-db')
    def send_json_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = TCPServer(server_address, MyHandler)
    print('Serveur démarré sur le port 8080...')
    httpd.serve_forever()
