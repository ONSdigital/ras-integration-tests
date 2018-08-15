from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/surveys/add-survey')


def get_access_survey_button():
    sign_in_button = browser.find_by_id('sign_in_button')
    sign_in_button.click()


def enter_enrolment_code(enrolment_code):
    browser.driver.find_element_by_id('ENROLEMENT_CODE_FIELD').send_keys(enrolment_code)


def click_continue_button():
    browser.find_by_id('continue_button').click()
    browser.find_by_id('confirm_survey_button').click()
