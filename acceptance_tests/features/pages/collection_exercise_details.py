from os.path import abspath

from acceptance_tests import browser
from config import Config


def go_to(survey, period):
    browser.visit('{}/surveys/{}/{}'.format(Config.RESPONSE_OPERATIONS_UI, survey, period))


def get_page_title():
    return browser.find_by_name('page-ce-title').value


def get_collection_exercise_details():
    ce_details = {
        "survey_info": browser.find_by_name('survey-info').value,
        "period": browser.find_by_name('period').value,
        "user_description": browser.find_by_name('user-description').value
    }
    return ce_details


def load_collection_instrument():
    test_file = 'resources/collection_instrument_files/064_0001_201803.xlsx'
    browser.driver.find_by_id('ciFile').send_keys(abspath(test_file))
    browser.find_by_id('btn-load-ci').click()


def get_collection_instrument_success_text():
    return browser.find_by_id('collection-instrument-success').text


def click_survey_breadcrumb():
    browser.find_by_id('breadcrumb-2').click()
