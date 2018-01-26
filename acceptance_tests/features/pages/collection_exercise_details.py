from os.path import abspath

from acceptance_tests import browser
from config import Config


def go_to(survey, period):
    browser.visit('{}/surveys/{}/{}'.format(Config.RESPONSE_OPERATIONS_UI, survey, period))


def get_page_title():
    return browser.title


def get_collection_exercise_details():
    ce_details = {
        "survey_info": browser.find_by_name('survey-info').value,
        "survey_title": browser.find_by_name('survey-title').value,
        "period": browser.find_by_name('period').value,
        "user_description": browser.find_by_name('user-description').value
    }
    return ce_details


def get_collection_exercise_events():
    ce_events = {
        "mps": browser.find_by_name('mps-date').value,
        "go_live": browser.find_by_name('go-live-date').value,
        "return_by": browser.find_by_name('return-by-date').value,
        "first_reminder": browser.find_by_name('first-reminder-date').value,
        "exercise_end": browser.find_by_name('exercise-end-date').value
    }
    return ce_events


def load_collection_instrument(test_file):
    browser.driver.find_element_by_id('ciFile').send_keys(abspath(test_file))
    browser.find_by_id('btn-load-ci').click()


def select_wrong_file_type(test_file):
    browser.driver.find_element_by_id('ciFile').send_keys(abspath(test_file))


def get_collection_instrument_error_text():
    return browser.driver.find_element_by_id('ciFileErrorText').text


def get_collection_instrument_success_text():
    return browser.find_by_id('collection-instrument-success').text


def get_collection_instruments():
    tds = browser.find_by_id('collection-instruments-table').find_by_tag('tbody').find_by_tag('td')
    return list(map(lambda td: td.value, tds))


def get_error_header():
    return browser.find_by_id('error-header').text
