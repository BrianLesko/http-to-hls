import http.server
import socketserver

PORT = 8002

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set the correct MIME type for .m3u8 files
        if self.path.endswith('.m3u8'):
            self.send_header('Content-Type', 'application/vnd.apple.mpegurl')
        # Ensure CORS headers if needed (remove if not needed)
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

# Set the Handler to the custom class
Handler = MyHttpRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()