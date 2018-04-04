from acceptance_tests import browser
from config import Config


def go_to_find_respondent():
    browser.visit('{}/respondents/'.format(Config.RESPONSE_OPERATIONS_UI))


def search_respondent_by_email(email):
    browser.find_by_id('query').fill(email)
    browser.find_by_id('btn-search-respondent').click()


def no_results_found():
    return 'No results found' in browser.html


def get_respondent_details():
    respondent_details = {
        "name": browser.find_by_id('respondent-name').text,
        "email": browser.find_by_id('respondent-email').text
    }
    return respondent_details


def find_no_respondent_msg():
    page_src = browser.driver.page_source
    return page_src
