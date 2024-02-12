import json
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.handle_health()
        elif self.path == '/get':
            self.handle_get()
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/add':
            self.handle_add()
        else:
            self.send_error(404)

    def handle_health(self):
        self.send_json_response(200, {"status": "OK"})

    def handle_get(self):
        with self.get_db_connection() as cnx:
            cursor = cnx.cursor()
            query = ("SELECT * FROM iterator")
            cursor.execute(query)
            iterators = [{"state": state} for state in cursor]
            self.send_json_response(200, {"status": "ok", "iterators": iterators})

    def handle_add(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        value = data['value']
        with self.get_db_connection() as cnx:
            cursor = cnx.cursor()
            query = ("INSERT INTO iterator (state) VALUES (%s)")
            cursor.execute(query, (value,))
            cnx.commit()
            self.send_json_response(200, {"status": "ok", "message": "Iterator value added successfully"})

    def get_db_connection(self):
        return mysql.connector.connect(user='root', password='root', host='172.10.0.10', database='iterator-db')

    def send_json_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf8'))

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()