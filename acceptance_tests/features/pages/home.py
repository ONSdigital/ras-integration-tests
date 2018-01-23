from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.RESPONSE_OPERATIONS_UI)


def click_surveys_link():
    link = browser.find_by_name('surveys-link')
    link.click()
