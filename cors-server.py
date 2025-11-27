#!/usr/bin/env python3
"""Simple HTTP server with CORS enabled for testing STAC Browser locally."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    port = 8000
    server = HTTPServer(('', port), CORSRequestHandler)
    print(f'🌐 CORS-enabled server running at http://localhost:{port}/')
    print(f'📂 Serving: {server.server_name}')
    print(f'🗺️  Test with STAC Browser:')
    print(f'   https://radiantearth.github.io/stac-browser/#/external/localhost:{port}/catalog.json')
    print(f'\n✋ Press Ctrl+C to stop')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n👋 Server stopped')
        sys.exit(0)
