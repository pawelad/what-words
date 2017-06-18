# What words?

What words is a simple [Tornado][tornado] application that can count words
occurrences in passed URL and display them as a nice tag cloud. It also
has a simple, password protected word list view with all-time word count.

Made to finally play around with [Tornado][tornado] and [Google App Engine][gae].

Last seen at [what-words.appspot.com][what words]

# Running locally
What words uses environment variables to manage configuration variables. To
run it locally you need at least `SECRET_KEY` set (either explicitly or in
`.env` file). It exposes a WSGI server for running it in production but 
locally you can just run `app.py`:

```shell
$ export SECRET_KEY='...'
$ pip3 install -r requirements.txt
$ python what_words/app.py
```

One time operation of creating database tables (`what_words.db.create_tables`)
is also required.

Whole application was made with [Google App Engine][gae] in mind so deploying
it there should be as easy as running `gcloud app deploy app.yaml`.

# Configuration
What words uses `python-decouple` to manage configuration variables. You can
have a look at the settings file to see what values are configurable, but for
reference here are the ones that I use locally:

```shell
$ cat .env
DEBUG=True
DATABASE_URL=mysql://pawelad@localhost/what_words
ADMIN_PASSWORD=...
SECRET_KEY=..
SALT=...
```

## Contributions
Package source code is available at [GitHub][github].

Feel free to use, ask, fork, star, report bugs, fix them, suggest enhancements,
add functionality and point out any mistakes. Thanks!

## Authors
Developed and maintained by [Paweł Adamczak][pawelad].

Released under [MIT License][license].


[gae]: https://appengine.google.com/
[github]: https://github.com/pawelad/what-words
[license]: https://github.com/pawelad/what-words/blob/master/LICENSE
[pawelad]: https://github.com/pawelad
[tornado]: http://www.tornadoweb.org/
[what words]: https://what-words.appspot.com/
