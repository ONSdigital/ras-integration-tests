from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')


def sign_in_alternate_respondent():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')
    if '/sign-in' in browser.url:
        browser.driver.find_element_by_id('username').send_keys(Config.RESPONDENT_USERNAME)
        browser.driver.find_element_by_id('inputPassword').send_keys(Config.RESPONDENT_PASSWORD)
        browser.find_by_id('sign_in_button').click()


def signed_in_respondent_with_email(email):
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')
    if '/sign-in' in browser.url:
        browser.driver.find_element_by_id('username').send_keys(email)
        browser.driver.find_element_by_id('inputPassword').send_keys(Config.RESPONDENT_PASSWORD)
        browser.find_by_id('sign_in_button').click()
