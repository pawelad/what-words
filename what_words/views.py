"""
what_words views
"""
import tornado.web
from what_words.forms import URLForm


class URLFormHandler(tornado.web.RequestHandler):
    """
    Tornado handler for URL form view
    """
    def get(self):
        self.render('templates/url_form.html', form=URLForm())
