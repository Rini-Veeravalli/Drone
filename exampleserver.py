#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import urllib, cStringIO
from PIL import Image
from cgi import parse_header, parse_multipart

import urlparse
#import requests
PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_POST(self):
		self._set_headers()
		#ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		length = int(self.headers.getheader('content-length'))	
		#field_data = self.rfile.read(length)
		#fields = urlparse.parse_qs(field_data)
		
		postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
		#print urlparse(self.headers.getheader())

		print postvars

		parsed_path = urlparse.urlparse(self.path)
		params = dict([p.split('=') for p in parsed_path[4].split('&')])
		#except:
		#	params = {}
		#print field_data
		#print fields
		print params

		

		

	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/webpage.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()


#webcam-streamer
#flask camera video streaming
#base64 decode, split by comma
