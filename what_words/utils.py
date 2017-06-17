"""
what_words utils
"""
from collections import Counter
from string import punctuation

import nltk
import requests
from bs4 import BeautifulSoup


def get_words_count(url, limit=None):
    """
    Helper function for getting top words in passed URL

    :param url: website URL
    :type url: str
    :param limit: limit number of returned results
    :type limit: int
    :returns: sorted list of (word, count) tuples
    :rtype: list of tuple
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    # Remove inline '<script>' and '<style>' tags
    for script in soup(['script', 'style']):
        script.decompose()

    text = soup.get_text().replace('\n', ' ')

    # Try to keep only nouns and verbs
    try:
        tokens = nltk.word_tokenize(text)
        # Remove punctuation and make lowercase
        tokens = [token.rstrip(punctuation).lower() for token in tokens]
        # Filter non alphabetic strings
        tokens = [token for token in tokens if token.isalpha()]
        tagged_tokens = nltk.pos_tag(tokens)

        # Tag needs to start wit N or V
        # http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
        words = [t[0] for t in tagged_tokens if t[1][0] in ['N', 'V']]
    except LookupError:
        words = [x.rstrip(punctuation).lower() for x in text.split()]

    c = Counter(words)

    return c.most_common(n=limit)
