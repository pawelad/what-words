"""
what_words main application
"""
from pathlib import Path

import nltk
import tornado.web
import tornado.wsgi
import wsgiref.simple_server
from decouple import config

from what_words import views


nltk.download(['punkt', 'averaged_perceptron_tagger'])


BASE_DIR = Path(__file__).parent

settings = {
    'debug': config('DEBUG', default=False, cast=bool),
    'cookie_secret': config('SECRET_KEY'),
    'static_path': str(BASE_DIR / 'static'),
    'xsrf_cookies': True,
    'login_url': '/login',
}


tornado_app = tornado.web.Application([
    tornado.web.url(r'/', views.URLFormHandler, name='index'),
    tornado.web.url(r'/login', views.LoginHandler, name='login'),
    tornado.web.url(r'/logout', views.LogoutHandler, name='logout'),
    tornado.web.url(r'/words', views.WordListHandler, name='word_list'),
], **settings)
wsgi_app = tornado.wsgi.WSGIAdapter(tornado_app)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8888, wsgi_app)
    server.serve_forever()
