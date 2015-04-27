#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Engler'
SITENAME = 'Wayfaring Coder'
SITEURL = ''

PATH = 'content'
THEME = 'pelican-bootstrap3'

TIMEZONE = 'Europe/Paris'

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
