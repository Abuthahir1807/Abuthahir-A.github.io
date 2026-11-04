from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import sys

class StaticHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if any(self.path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg', '.woff2', '.pdf']):
            self.send_header('Cache-Control', 'public, max-age=86400')
        else:
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    port = 8000
    server = ThreadingHTTPServer(('127.0.0.1', port), StaticHandler)
    print(f"Server started at http://localhost:{port}")
    sys.stdout.flush()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
