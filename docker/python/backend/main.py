# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import mysql.connector

# Créez une connexion à la base de données
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='iterator-db'
)

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get':
            response = self.get_iterator_status()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(response, 'utf-8'))
        else:
            super().do_GET()

    def get_iterator_status(self):
        # Utilisez la connexion à la base de données pour obtenir l'état de l'itérateur ici
        cursor = db_connection.cursor()
        cursor.execute("SELECT state FROM iterator")
        state = cursor.fetchone()[0]
        cursor.close()

        return f'{{"status": "OK", "iterator": {state}}}'

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = TCPServer(server_address, MyHandler)

    print('Serveur démarré sur le port 8000...')
    httpd.serve_forever()
