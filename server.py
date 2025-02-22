import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/website/index.html'
        try:
            with open(self.path[1:], 'r', encoding='utf-8') as f:
                file_to_open = f.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=UTF-8')
            self.end_headers()

        except FileNotFoundError:
            file_to_open = "File not found"
            self.send_response(404)
            self.end_headers()

        self.wfile.write(bytes(file_to_open, 'utf-8'))

import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/website/index.html'
        try:
            with open(self.path[1:], 'r', encoding='utf-8') as f:
                file_to_open = f.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=UTF-8')
            self.end_headers()

        except FileNotFoundError:
            file_to_open = "File not found"
            self.send_response(404)
            self.end_headers()

        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 9000), Serv)
httpd.serve_forever()
