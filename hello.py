# -*- coding: utf-8 -*-
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting',  "hello")
        self.write(greeting + ', friendly user!')
        # self.render("test.html")

# class BlogHandler(tornado.web.RequestHandler):
#     def get(self):
#         coll = self.application.db.blog
#         blog = coll.find_one()
#         if blog:
#             self.render("blog.html",
#             page_title = blog['title'],
#             blog = blog,
#             )
#         else:
#             self.redirect('/')


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        hello = "Oh, Help me!"
        self.render("index.html", hello=hello)

    def post(self):
        arry = ['PHP', 'MySQL', 'SQL', 'PostgreSQL', 'HTML', 'CSS','666', 'HTML5', 'CSS3', 'JSON']
        return arry

if __name__ == "__main__":
    print 'Development server running on "http://localhost:8888"'
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler),
                  (r"/test", TestHandler)
                  ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
