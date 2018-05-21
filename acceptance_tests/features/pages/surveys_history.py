from acceptance_tests import browser
from common.browser_utilities import is_text_present_with_retry


def go_to_history_tab():
    browser.find_by_id('SURVEY_HISTORY_TAB').click()


def get_cases():
    is_text_present_with_retry('Trading as:', delay=3, retries=10)
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
                 if ru_ref in case['business_details']))


def get_status_text():
    return browser.find_by_id('status-1').text
