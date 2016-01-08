#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Engler'
SITENAME = "Wayfaring Coder: Will Engler's Blog"
# http://willengler.github.io
SITEURL = 'http://willengler.github.io'

PATH = 'content'
THEME = 'pelican-bootstrap3'
FAVICON = 'images/favicon.ico'
DISQUS_SITENAME = "wayfaringcoder"

ABOUT_ME = """I'm a software developer living in Chicago.
              This blog is a place for reflections on technology and culture."""

AVATAR = 'images/monteverde/willVista.JPG'
BOOTSTRAP_THEME = 'united'

TIMEZONE = 'America/Chicago'

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
          ('Github', 'https://github.com/WillEngler'),
          ('My Job', 'http://plenar.io/'))

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images']
