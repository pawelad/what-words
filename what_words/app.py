"""
what_words main application
"""
from pathlib import Path

import tornado.web
import tornado.wsgi
import wsgiref.simple_server

from what_words.views import URLFormHandler


BASE_DIR = Path(__file__).parent


settings = {
    'debug': True,
    'static_path': str(BASE_DIR / 'static'),
}


tornado_app = tornado.web.Application([
    (r'/', URLFormHandler),
], **settings)
wsgi_app = tornado.wsgi.WSGIAdapter(tornado_app)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8888, wsgi_app)
    server.serve_forever()
