"""
what_words main application
"""
from pathlib import Path

import nltk
import tornado.web
import tornado.wsgi
import wsgiref.simple_server
from decouple import config

from what_words.views import URLFormHandler


nltk.download(['punkt', 'averaged_perceptron_tagger'])


BASE_DIR = Path(__file__).parent

settings = {
    'debug': config('DEBUG', default=False, cast=bool),
    'static_path': str(BASE_DIR / 'static'),
}


tornado_app = tornado.web.Application([
    (r'/', URLFormHandler),
], **settings)
wsgi_app = tornado.wsgi.WSGIAdapter(tornado_app)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8888, wsgi_app)
    server.serve_forever()
