#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pelly'
SITENAME = 'blog.vegaswalker.net'
SITEURL = 'http://blog.vegaswalker.net'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins/pelican-plugins']
PLUGINS = [u"disqus_static",]

DISQUS_SITENAME = u'vegaswalker-blog'
DISQUS_SECRET_KEY = u'dRH1AJdfVsjprKvS6Qvn6pMrfrWiZXTH2bHTnnyH4KlGmew7vUOJ9GZaG22QuiHs'
DISQUS_PUBLIC_KEY = u'AFmdfJf8WRPkf9t2Bq2SXJCZO0sDVkRi9Wx3UQsAARMtQ0UQjG2ZixBEylObJGtv'
