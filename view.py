import http.server
import socketserver

def serve_content(port, directory):
    handler = http.server.SimpleHTTPRequestHandler
    handler.directory = directory

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving HLS content at port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    serve_content(8001, "./hls_content")