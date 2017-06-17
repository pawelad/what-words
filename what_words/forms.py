"""
what_words forms
"""
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired
from wtforms_tornado import Form


class URLForm(Form):
    """
    Simple URL form
    """
    url = URLField(
        label='URL',
        description="Enter URL to see what words are there",
        validators=[InputRequired()],
    )
