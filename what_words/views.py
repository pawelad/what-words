"""
what_words views
"""
import json

import requests
import tornado.web

from what_words.forms import URLForm
from what_words.utils import get_words_count


class URLFormHandler(tornado.web.RequestHandler):
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
                word_count = get_words_count(url, limit=100)
            except requests.RequestException:
                form.url.errors.append("Passed URL is inaccessible.")
                return self.render('templates/url_form.html', form=form)

            # Transform the data for the word cloud plugin
            json_word_count = json.dumps(word_count)

            ctx = {
                'url': url,
                'word_count': json_word_count,
            }

            return self.render('templates/words_list.html', **ctx)

        return self.render('templates/url_form.html', form=form)
