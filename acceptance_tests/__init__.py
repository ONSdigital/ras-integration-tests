import os

from splinter import Browser

if os.getenv('HEADLESS', 'True') == 'True':
    browser = Browser('chrome', headless=True)
else:
    browser = Browser('chrome')
