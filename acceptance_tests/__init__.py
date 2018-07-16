import logging
import os

from retrying import retry
from selenium import webdriver
from splinter import Browser
from structlog import configure
from structlog.stdlib import LoggerFactory

logging.basicConfig()
configure(logger_factory=LoggerFactory())


@retry(retry_on_exception=lambda e: isinstance(e, ConnectionError), wait_fixed=1000, stop_max_attempt_number=30)
def create_browser():
    if os.getenv('HEADLESS', 'True') == 'True':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        return Browser('chrome', headless=True, options=chrome_options)
    else:
        return Browser('chrome')


browser = create_browser()
