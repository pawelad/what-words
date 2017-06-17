"""
what_words views
"""
import json

import requests
import tornado.web
from decouple import config

from what_words.db import PeeweeRequestHandler
from what_words.forms import LoginForm, URLForm
from what_words.models import WordCount
from what_words.utils import get_words_count


ADMIN_PASSWORD = config('ADMIN_PASSWORD')


class LoginHandler(tornado.web.RequestHandler):
    """
    Tornado handler for login view
    """
    def get(self):
        """
        Render login form
        """
        form = LoginForm(self.request.arguments or None)

        return self.render('templates/login_form.html', form=form)

    def post(self):
        """
        Login the user if he entered correct admin password

        :return:
        """
        form = LoginForm(self.request.arguments or None)
        password = self.get_argument('password', '')

        if password == ADMIN_PASSWORD:
            self.set_secure_cookie('user', b'')
            return self.redirect('/')
        else:
            form.password.errors = ("Incorrect password.",)
            return self.render('templates/login_form.html', form=form)


class URLFormHandler(PeeweeRequestHandler):
    """
    Tornado handler for URL form view
    """
    def get(self):
        """
        Render URL form
        """
        form = URLForm(self.request.arguments or None)

        return self.render('templates/url_form.html', form=form)

    def post(self):
        """
        Display top 100 words from passed URL and save words counters
        to the database
        """
        form = URLForm(self.request.arguments or None)

        if form.validate():
            url = form.data['url']
            try:
                word_list = get_words_count(url, limit=100)
            except requests.RequestException:
                form.url.errors = ("Passed URL is inaccessible.",)
                return self.render('templates/url_form.html', form=form)

            # Save word counts to the database
            for word_count in word_list:
                word_hash = WordCount.word_hash(word_count[0])

                word, _ = WordCount.get_or_create(
                    id=word_hash,
                    defaults={
                        'word': word_count[0],
                    }
                )
                word.count += word_count[1]
                word.save()

            # Transform the data for the word cloud plugin
            json_word_list = json.dumps(word_list)

            ctx = {
                'url': url,
                'word_list': json_word_list,
            }

            return self.render('templates/words_list.html', **ctx)

        return self.render('templates/url_form.html', form=form)
