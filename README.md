# Progjar

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.writeHtml( "ini konten", 500)

    def writeHtml(self,content, rspCode):                    
        self.send_response(rspCode)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if rspCode == 200 :
            self.wfile.write(bytes("<html><head><title>web server ok</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>"+ content +"</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else :
            self.wfile.write(bytes("<html><head><title>error %s</title></head>" % rspCode, "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<h1>error %s.</h1>" % rspCode, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
