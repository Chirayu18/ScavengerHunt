#!/usr/bin/env python3
"""
Simple HTTPS server for testing the Scavenger Hunt app locally.
HTTPS is required for the Geolocation API to work on most browsers.

Usage:
    python server.py

Then open https://localhost:8443 in your browser.
You'll need to accept the self-signed certificate warning.
"""

import http.server
import ssl
import os

PORT = 8443

# Generate self-signed certificate if it doesn't exist
if not os.path.exists('cert.pem') or not os.path.exists('key.pem'):
    print("Generating self-signed SSL certificate...")
    os.system('openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"')
    print("Certificate generated!")

print(f"""
╔══════════════════════════════════════════════════════════════╗
║                   A Journey Through Us                       ║
║                    Scavenger Hunt App                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Server starting on: https://localhost:{PORT}                  ║
║                                                              ║
║  ⚠️  Your browser will show a security warning because       ║
║     we're using a self-signed certificate.                   ║
║                                                              ║
║  → Click "Advanced" → "Proceed to localhost"                 ║
║                                                              ║
║  📱 To test on your phone (same WiFi network):               ║
║     1. Find your computer's IP address                       ║
║     2. Open https://YOUR_IP:{PORT} on your phone              ║
║     3. Accept the certificate warning                        ║
║                                                              ║
║  Press Ctrl+C to stop the server                             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

# Create HTTPS server
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('0.0.0.0', PORT), handler)

# Wrap with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\nServer stopped. Goodbye! ♥")
    httpd.shutdown()
