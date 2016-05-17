#coding:utf-8

import json
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8200, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", RegisterHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "test_index.html",
            page_title = "Tornado | Home",
            header_text = "Demo1!",
            footer_text = "--2015--"
        )
class RegisterHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render("regist.html")

    def post(self, *args, **kwargs):
        mobile = self.get_argument("mobile")
        password = self.get_argument("password")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
