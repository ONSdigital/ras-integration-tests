from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/surveys/add-survey')


def get_access_survey_button():
    sign_in_button = browser.find_by_id('SIGN_IN_BUTTON')
    sign_in_button.click()
