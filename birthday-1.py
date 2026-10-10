"""
Anis Chacha Birthday Website
Python Essentials 1: uses only basic Python to start a local web server.
The website itself is written in HTML.
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Open the folder containing this Python file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

address = ("", 8000)
server = HTTPServer(address, SimpleHTTPRequestHandler)

print("Birthday website is running!")
print("Open this address in your browser: http://localhost:8000")
print("Press Ctrl+C to stop the server.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nBirthday website stopped.")
    server.server_close()
