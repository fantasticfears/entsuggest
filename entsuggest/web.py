import os.path

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("root.html")


def make_app():
  dir_name = os.path.dirname(__file__)
  settings = {
    "static_path": os.path.join(dir_name, "assets"),
    "xsrf_cookies": True,
    "template_path": os.path.join(dir_name, "views"),
    "debug": True,
  }

  return tornado.web.Application([
      (r"/", MainHandler),
  ], **settings)


if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()
