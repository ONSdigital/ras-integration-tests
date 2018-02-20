from os.path import abspath

from acceptance_tests import browser
from config import Config


def go_to(survey, period):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey}/{period}')


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


def get_loaded_sample():
    tds = browser.find_by_id('sample-table').find_by_tag('tbody').find_by_tag('td')
    return list(map(lambda td: td.value, tds))


def get_collection_exercise_events():
    ce_events = {
        "mps": browser.find_by_name('mps-date').value,
        "go_live": browser.find_by_name('go-live-date').value,
        "return_by": browser.find_by_name('return-by-date').value,
        "first_reminder": browser.find_by_name('first-reminder-date').value,
        "exercise_end": browser.find_by_name('exercise-end-date').value,
        "ref_period_start": browser.find_by_name('period-start-date').value,
        "ref_period_end": browser.find_by_name('period-end-date').value,
        "employment": browser.find_by_name('employment-date').value,
        "second_reminder": browser.find_by_name('second-reminder-date').value,
        "third_reminder": browser.find_by_name('third-reminder-date').value
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


def get_status():
    return browser.find_by_id('ce_status').text
