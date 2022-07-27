from http.server import BaseHTTPRequestHandler
import json , requests , random

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        url = requests.get("https://onetext.cicada000.work/Data.json")
        text = url.text
        OneTextRaw = json.loads(text)
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(OneTextRaw.encode())
        
        return
