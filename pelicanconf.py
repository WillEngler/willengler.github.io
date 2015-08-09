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

ABOUT_ME = """I'm a recent college grad beginning his career
              in software development. I'm on the job market,
              so please get in touch if you're hiring."""
AVATAR = 'images/monteverde/willVista.JPG'
BOOTSTRAP_THEME = 'united'

TIMEZONE = 'America/Panama'

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
          ('Resumé', 'http://will-resume.bitballoon.com/'))

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images']
