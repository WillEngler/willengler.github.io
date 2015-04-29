#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Engler'
SITENAME = 'Wayfaring Coder'
SITEURL = 'http://willengler.github.io'

PATH = 'content'
THEME = 'pelican-bootstrap3'
FAVICON = 'images/favicon.ico'
DISQUS_SITENAME = "wayfaringcoder"

ABOUT_ME = "Right now I'm wandering Latin America while trying to learn more about making good software."
AVATAR = 'images/arch.jpg'
BOOTSTRAP_THEME = 'united'

TIMEZONE = 'America/Costa_Rica'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = None

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/WillEngler'),
          ('Github', 'https://github.com/WillEngler'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images']
