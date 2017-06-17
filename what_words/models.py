"""
what_words models
"""
import peewee
from decouple import config
from passlib.hash import pbkdf2_sha256

from what_words.db import db


class WordCount(peewee.Model):
    """
    Simple model that represents a word and number of its occurrences
    """
    id = peewee.CharField(primary_key=True, unique=True, index=True)
    word = peewee.CharField()
    count = peewee.IntegerField(default=0)

    class Meta:
        database = db

    @staticmethod
    def word_hash(word, salt=None):
        """
        Helper method for calculating word hash

        :param word: word to hash
        :type word: str
        :param salt: hash salt
        :type salt: bytes
        :returns: word hash
        :rtype: str
        """
        # Try to take salt value from environment variable
        if salt is None:
            salt = config('SALT', default=b'')

        if isinstance(salt, str):
            salt = str.encode(salt)

        return pbkdf2_sha256.hash(word, salt=salt)
