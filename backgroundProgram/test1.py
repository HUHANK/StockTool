# -*- coding:utf-8 -*-

import tushare as ts
import urllib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import BaseHTTPServer
from SocketServer import ThreadingMixIn


def execfunc(funcname, param, module='tushare'):
    main = sys.modules[module]

    if not hasattr(main, funcname):
        raise Exception(str(module)+" module hasn't function: "+str(funcname))
    return getattr(main, funcname)(param)


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print "########################"
        print self.path
        uri = urllib.unquote(self.path)
        method = ''
        param = ''
        if '?' in uri:
            arr = uri.split("?")
            method = arr[0].strip("/")
            param = arr[1]
        else:
            method = uri.strip("/")

        if len(method) < 1:
            self.wfile.write("Hello World!\n")
            return
        print "method: %s" % method
        print "Param: %s" % param
        res = execfunc(method, param)
        res = res.to_json()
        #print res

        #SEND
        self.send_response(200)
        self.send_header("Conten-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Conten-Length", str(len(res)))
        self.end_headers()
        self.wfile.write(res)


class ThreadedHTTPServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    """Handle request in a separete thread"""

def start_server(port):
    print "Now Start HttpServer: PORT=" + str(port) + "..."
    http_server = ThreadedHTTPServer(("", int(port)), RequestHandler)
    http_server.serve_forever()


start_server(6688)
