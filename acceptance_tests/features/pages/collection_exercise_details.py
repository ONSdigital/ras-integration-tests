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


def select_sample():
    test_file = 'resources/sample_files/business-survey-sample-date.csv'
    browser.driver.find_element_by_id('sampleFile').send_keys(abspath(test_file))


def load_sample():
    select_sample()
    browser.find_by_id('btn-load-sample').click()


def get_sample_success_text():
    return browser.find_by_id('sample-success').first.text


def has_sample_preview():
    element_ids = ['sample-preview-businesses', 'sample-preview-ci', 'sample-preview']
    elements = []

    for element_id in element_ids:
        elements.append(browser.find_by_id(element_id))

    for element in elements:
        if element.is_empty():
            return False

    return True


def cancel_sample_preview():
    browser.find_by_id('btn-cancel-load-sample').click()
