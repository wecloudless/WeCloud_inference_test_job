from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket
import cgi
from cgi import parse_header, parse_multipart
import urllib.request
import io,shutil
import re

from classify_demo import classify_demo

class HTTPServerHandler(BaseHTTPRequestHandler):
    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())

    def do_GET(self):        # get
        self.send_error(404, "Page not Found!")
        return
        # print(self.requestline)
        # if self.path != '/hello':
        #     self.send_error(404, "Page not Found!")
        #     return

        # data = {
        #     'result_code': '1',
        #     'result_desc': 'Success',
        #     'timestamp': '',
        #     'data': {
        #         'message_id': '25d55ad283aa400af464c76d713c07ad'
        #     }
        # }
        # self.send_response(200)
        # self.send_header('Content-type', 'application/json')
        # self.end_headers()
        # self.wfile.write(json.dumps(data).encode())

    def do_POST(self):         # post
        req_data = self.rfile.read(int(self.headers['content-length'])) 
        res1 = re.match(re.compile(b"-+\w*\s{2}(.*?\s{2}){2}\s{2}"), req_data)
        res2 = re.search(re.compile(b"\s{2}-+.+\s{2}"), req_data)
        file_data = req_data[res1.end():res2.start()]  

        #
        with open("test/classify.jpg", "wb") as w:
            w.write(file_data)
        classify_res = classify_demo("test/classify.jpg")

        data = {
                'result_code': '2',
                'result_desc': 'Success',
                'timestamp': '',
                'data': classify_res
        }
        #
        self.send_response(200)   #
        self.send_header('Content-type', 'application/json') #
        self.end_headers()  #
        self.wfile.write(json.dumps(data).encode('utf-8'))   #


if __name__ == '__main__':
    try:
        server = HTTPServer(('127.0.0.1', 12344), HTTPServerHandler)
        print("Starting server, listen at: 12344")
        # server.serve_forever()
    except:
        pass
    print("test for example")