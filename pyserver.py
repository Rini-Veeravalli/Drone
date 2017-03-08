#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SocketServer

class S(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		#self.wfile.write("<html><body><h1>hi!</h1></body></html>")

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		# Doesn't do anything with posted data
		self._set_headers()
		#self.wfile.write("<html><body><h1>POST!</h1></body></html>")

	def do_PUT(self):
		self._set_headers()
		#deal with the & and parsing the url
		function handle(request, response) {
			request.on('data', add);
			request.on('end', end);
			var body = "";
			function add(chunk) {
				body = body + chunk.toString();
			}
			function end() {
				console.log("Body:", body);
				reply(response);
			}
		}

def run(server_class=HTTPServer, handler_class=S, port=8081):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'Starting httpd...'
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
