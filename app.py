#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.print_request()

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()
        self.print_request()

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.print_request()

    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        self.print_request()

    def do_PATCH(self):
        self.send_response(200)
        self.end_headers()
        self.print_request()

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.print_request()

    def print_request(self):
        print(f"+ {self.command} {self.path}\n")
        # Print headers
        print(f"{self.headers}")
        # Print payload if it exists    
        content_len = int(self.headers.get('content-length', 0))
        if content_len > 0:
            payload = self.rfile.read(content_len)
            print(f"{payload}")


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")