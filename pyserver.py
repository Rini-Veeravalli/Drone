#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SocketServer
import urlparse
import requests

class S(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_HEAD(self):
		self._set_headers()

	def do_PUT(self):
		self._set_headers()
			#deal with the & and parsing the url
			#pip install furl - unlicensed in public domain, supports Python 2 & 3
		#from furl import furl
		#f = furl('oneclick_url')
			#f is a fragment, with a path and query separated by '?'
		#print f.args['clickcoord_x']
		#print f.args['clickcoord_y']		
		#print f.args['i_width']
		#print f.args['i_height']

		url = oneclick_url
		parsed = urlparse.urlparse(url)
		print urlparse.parse_qs(parsed.query)['clickcoord_x']

		self.wfile.write("<html><body><h1>POST!</h1></body></html>")
		self.wfile.write("clickcoord_x")

		response = 'Selection sent'
		#function handle(request, response) {
			#reads the body of the request
			#request.on('data', add);
			#request.on('end', end);
			#var body = "";
			#function add(chunk) {
			#	body = body + chunk;
			#}
			#function end() {
			#	console.log("Body:", body);
			#	reply(response);
			#}
		#}

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
