#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import textwrap

import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options

from tornado.options import options, define
define('port', default=8000, help='run on the given port', type=int)

class ReverseHander(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandHander(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/reverse/(\w+)', ReverseHander),
            (r'/wrap', WrapHandHander)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

