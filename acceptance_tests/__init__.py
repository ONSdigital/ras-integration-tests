import logging
import os

from splinter import Browser
from structlog import configure
from structlog.stdlib import LoggerFactory

logging.basicConfig()
configure(logger_factory=LoggerFactory())

if os.getenv('HEADLESS', 'True') == 'True':
    browser = Browser('phantomjs')
else:
    browser = Browser('chrome')
