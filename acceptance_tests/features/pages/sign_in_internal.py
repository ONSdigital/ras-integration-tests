from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.RESPONSE_OPERATIONS_UI + '/sign-in')


def enter_username():
    browser.driver.find_element_by_id('username').send_keys(str(Config.INTERNAL_USERNAME))


def enter_password():
    browser.driver.find_element_by_id('password').send_keys(str(Config.INTERNAL_PASSWORD))


def internal_sign_in_btn():
    browser.find_by_id('SIGN_IN_BUTTON').click()
