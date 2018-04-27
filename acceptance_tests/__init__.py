import logging
import os

from selenium import webdriver
from splinter import Browser
from structlog import configure
from structlog.stdlib import LoggerFactory

logging.basicConfig()
configure(logger_factory=LoggerFactory())

if os.getenv('HEADLESS', 'True') == 'True':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1200")
    browser = Browser('chrome', headless=True, options=chrome_options)
else:
    browser = Browser('chrome')
