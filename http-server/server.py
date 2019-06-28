import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8080


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.post_data = None
        paths = {
            '/logged': {'status': 200},
            '/js': {'status': 200},
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        self.post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self.respond({'status': 200})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = ''''''
        if path == "/logged" and self.post_data != None:
            temp = self.post_data.decode('utf-8').split("&")
            data = {}
            for e in temp:
                data[e.split("=")[0]] = e.split("=")[1]
            if data["login"] == "little_cat" and data["password"] == "is_cute":
                content = '''<html><body>logged in!</body></html>'''
            else:
                content = '''<html><body>Wrong credentials! Read instruction!</body></html>'''

        elif path == "/js":
            content = '''
            <html><head><title>Simple webpage to be scrapped.</title>
            <script>
                function jsLoad(){
                    document.getElementById("insertData").innerHTML="secret data";
                };
            </script></head>
            <body>
                <div id="insertData"></div>
                <button id="click-me" onclick="jsLoad()">click me!</button>
            </body></html>
            '''


        else:
            content = '''
            <html><head><title>Simple webpage to be scrapped.</title></head>
            <body><form action="logged" method=POST><input type="text" name="login" id="login" /><input type=password name="password" id="password"><input type=submit id="submit_button"></form>
            </body></html>
            '''.format(path)
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
