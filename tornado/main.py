# -*- coding:utf-8 -*-

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
import tornado.web
import tornado.httpserver
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


handlers=[
    (r'/', IndexHandler),
    (r'^/()$', tornado.web.StaticFileHandler, {
        "path": os.path.join(os.path.dirname(__file__), "statics"),
        "default_filename":"index.html"
    }),
]

settings={
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "statics"),
    "debug": True
}

if __name__ == "__main__":
    app = tornado.web.Application(handlers, **settings)

    app.listen(8000)

    tornado.ioloop.IOLoop.current().start()