import time

from acceptance_tests import browser
from common.browser_utilities import is_text_present_with_retry


def go_to_history_tab():
    browser.find_by_id('SURVEY_HISTORY_TAB').click()


def refresh_history_until_survey_for_ru_found(ru_ref):
    for _ in range(12):
        go_to_history_tab()
        case = get_case(ru_ref)
        if case:
            return True
        time.sleep(5)


def get_cases():
    is_text_present_with_retry('Trading as:', delay=5, retries=10)
    case_list = browser.find_by_id('survey-list').find_by_name('survey-card')
    cases = [{
                 "survey": case.find_by_id('SURVEY_NAME').text,
                 "business_details": case.find_by_name('reporting-unit-details').text,
                 "period": case.find_by_name('period').text,
                 "status": case.find_by_name('status').text
             } for case in case_list]
    return cases


def get_case(ru_ref):
    return next((case for case in get_cases()
                 if ru_ref in case['business_details']), None)


def get_status_text():
    return browser.find_by_id('status-1').text
