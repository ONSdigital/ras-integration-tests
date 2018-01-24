import os

from splinter import Browser


if os.getenv('HEADLESS', 'True') == 'True':
    browser = Browser('phantomjs')
else:
    browser = Browser('chrome')
