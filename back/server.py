#! /usr/bin/env python

import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

from os import curdir, sep
import cgi, sys, re, os, json, zipfile, subprocess, random


PORT = '9001'
tid = 0

class handler (BaseHTTPRequestHandler):

    def do_GET(self):
        print self.path
        if self.path=="/":
            self.path="/front/index.html"
        else:
            self.path="/front" + self.path

        print self.path

        try:
            mime = None
            if self.path.endswith(".html"):
                mime='text/html'
            if self.path.endswith(".js"):
                mime='application/javascript'
            if self.path.endswith(".jpg"):
                mime='image/jpg'
            if self.path.endswith(".jpeg"):
                mime='image/jpg'
            if self.path.endswith(".gif"):
                mime='image/gif'
            if self.path.endswith(".png"):
                mime='image/png'
            if self.path.endswith(".css"):
                mime='text/css'
            if self.path.endswith(".eot"):
                mime='font/opentype'
            if self.path.endswith(".svg"):
                mime='font/opentype'
            if self.path.endswith(".ttf"):
                mime='font/opentype'  
            if self.path.endswith(".woff"):
                mime='font/opentype'                                                                                    



            if mime:
                file = open(curdir + sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type',mime)
                self.end_headers()
                self.wfile.write(file.read())
                file.close()
                return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    #make doPOST method


try:
    server = BaseHTTPServer.HTTPServer(('', 9001), handler)
    print 'Starting ChessMate server on port ' + PORT + '!\n'
    server.serve_forever()

except KeyboardInterrupt:
    print 'Exiting...\nThank you for using the server! Have a pleasant day :)!\n'
    os.system("rm -rf data/env/* data/checks/* data/results/*")
    server.socket.close()
    exit(0)
