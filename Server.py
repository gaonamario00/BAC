from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import json

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/login.html'
        return super().do_GET()

    def cargar_usuarios(self):
        try:
            with open('usuarios.txt', 'r') as file:
                usuarios = json.load(file)
        except FileNotFoundError:
            usuarios = []
        return usuarios

if __name__ == "__main__":
    PORT = 8080
    handler = MyHandler

    with TCPServer(("", PORT), handler) as httpd:
        print(f"Servidor en ejecución en http://127.0.0.1:{PORT}/")
        httpd.serve_forever()
