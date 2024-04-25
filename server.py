import http.server
import os

def handle_get_request(self):
    try:
        if self.path == '/styles.css':
            with open(os.path.join(os.path.dirname(__file__), 'styles.css'), 'rb') as file:
                content = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/script.js':
            with open(os.path.join(os.path.dirname(__file__), 'script.js'), 'rb') as file:
                content = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/':
            with open(os.path.join(os.path.dirname(__file__), 'chat.html'), 'rb') as file:
                content = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404, 'File not found')

    except FileNotFoundError:
        self.send_error(404, 'File not found')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    do_GET = handle_get_request

if __name__ == '__main__':
    httpd = http.server.HTTPServer(('localhost', 8080), MyHTTPRequestHandler)
    httpd.serve_forever()