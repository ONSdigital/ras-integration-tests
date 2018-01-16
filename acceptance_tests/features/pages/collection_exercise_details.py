from os.path import abspath

from acceptance_tests import browser
from config import Config


def go_to(survey, period):
    browser.visit('{}/surveys/{}/{}'.format(Config.RESPONSE_OPERATIONS_UI, survey, period))


def get_collection_exercise_details():
    ce_details = {
        "survey_info": browser.find_by_name('survey-info').value,
        "period": browser.find_by_name('period').value,
        "user_description": browser.find_by_name('user-description').value
    }
    return ce_details


def load_sample():
    test_file = 'acceptance_tests/features/test_data/business-survey-sample-date.csv'
    browser.driver.find_element_by_id('sampleFile').send_keys(abspath(test_file))
    browser.find_by_id('btn-load-sample').click()


def get_sample_success_text():
    return browser.find_by_id('sample-success').text
