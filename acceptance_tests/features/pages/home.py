from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.RESPONSE_OPERATIONS_UI)


def click_surveys_link():
    link = browser.find_by_name('surveys-link')
    link.click()


def verify_messages_link_present():
    messages_link = browser.find_by_id('messages-link')
    if messages_link:
        return True
    else:
        return False


def go_to_external_home():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')
