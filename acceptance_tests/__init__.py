import logging
import os

from retrying import retry
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from splinter import Browser
from structlog import configure
from structlog.stdlib import LoggerFactory
from urllib3.exceptions import ProtocolError


logging.basicConfig()
configure(logger_factory=LoggerFactory())


def web_driver_connection_error(e):
    return isinstance(e, ConnectionError) or isinstance(e, ProtocolError)


@retry(retry_on_exception=web_driver_connection_error, wait_fixed=1000, stop_max_attempt_number=30)
def create_browser():
    driver_type = os.getenv('WEBDRIVER', 'chrome').lower()
    headless = os.getenv('HEADLESS', 'True') == 'True'

    if driver_type == 'chrome':
        chromedriver_binary.add_chromedriver_to_path()
        os.chmod(chromedriver_binary.chromedriver_filename, 0o755)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return Browser(driver_type, headless=headless, options=chrome_options)

    # if driver_type == 'firefox':
    #     firefox_options = webdriver.FirefoxOptions()
    #     binary_path = firefox_options.binary_location
    #     binary = FirefoxBinary(binary_path)
    #     driver = webdriver.Firefox(firefox_binary=binary)
    #     return Browser(driver_type, headless=headless, options=firefox_options)

    return Browser(driver_type, headless=headless)


browser = create_browser()
browser.driver.set_window_size(1920, 1080)
