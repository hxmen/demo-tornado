import textwrap

import tornado.ioloop
import tornado.web
import tornado.websocket


class EchoHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message('connected')

    def on_message(self, message):
        self.write_message(message)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'user')
        self.write("Hello " + greeting + ", tornado world")

    def write_error(self, status_code, **kwargs):
        self.write('You got a %d error.' % status_code)


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))


    def get(self):
        self.write('a')


def make_app():
    return tornado.web.Application([
        (r"/r/(\w+)", ReverseHandler),
        (r"/w", MainHandler),
        (r"/", WrapHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
