from acceptance_tests import browser
from common.browser_utilities import wait_for_url_matches_one_of
from config import Config
from logging import getLogger
from structlog import wrap_logger


logger = wrap_logger(getLogger(__name__))


def go_to():
    target_url = Config.RESPONSE_OPERATIONS_UI + '/sign-in'
    alternate_url = Config.RESPONSE_OPERATIONS_UI + '/'
    browser.visit(target_url)
    wait_for_url_matches_one_of(target_url, alternate_url, timeout=10, retry=1, post_change_delay=0.5)


def get_page_title():
    return browser.title


def enter_correct_username(user_name):
    browser.driver.find_element_by_id('username').send_keys(user_name)


def enter_incorrect_username():
    browser.driver.find_element_by_id('username').send_keys('someone')


def enter_correct_password():
    browser.driver.find_element_by_id('password').send_keys(str(Config.INTERNAL_PASSWORD))


def enter_incorrect_password():
    browser.driver.find_element_by_id('password').send_keys('words')


def click_internal_sign_in_button():
    browser.find_by_id('SIGN_IN_BUTTON').click()


def check_username_required():
    browser.find_link_by_text('Please enter a username')


def check_password_required():
    browser.find_link_by_text('Please enter a password')


def authentication_retry_link():
    return browser.find_by_id('try-again-link')
