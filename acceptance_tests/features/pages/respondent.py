from acceptance_tests import browser
from config import Config


def go_to_find_respondent():
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/respondents/')


def search_respondent_by_email(email):
    browser.find_by_id('query').fill(email)
    browser.find_by_id('btn-search-respondent').click()


def no_results_found():
    return 'No results found' in browser.html


def get_respondent_details():
    respondent_details = {
        "email": browser.find_by_id('respondent-email').text,
        "name": browser.find_by_id('respondent-name').text,
        "telephone": browser.find_by_id('respondent-telephone').text,
        "account_status": browser.find_by_id('respondent-account-status').text
    }
    return respondent_details


def not_found():
    return 'No Respondent found' in browser.html
