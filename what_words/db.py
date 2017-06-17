"""
what_words database related code
"""
from decouple import config
from playhouse.db_url import connect
from tornado.web import RequestHandler


db = connect(config('DATABASE_URL', default='sqlite:///db.sqlite'))


class PeeweeRequestHandler(RequestHandler):
    """
    Simple `RequestHandler` class that explicitly manages peewee's
    database connection
    """
    def prepare(self):
        """
        Extends Tornado's default `prepare` method and connects to the database
        """
        db.connect()
        return super().prepare()

    def on_finish(self):
        """
        Extends Tornado's default `prepare` method and closes connection to
        the database
        """
        if not db.is_closed():
            db.close()
        return super().on_finish()


def create_tables():
    """
    Helper function for creating database tables.
    """
    from what_words.models import WordCount

    db.connect()
    db.create_tables([WordCount])
