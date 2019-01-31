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


def click_edit_contact_details():
    browser.find_by_id('edit-contact-details').click()


def click_resend_verification_email():
    browser.find_by_id('resend-email-verification-btn').click()


def click_change_enrolment_status(_):
    browser.find_by_id('change-enrolment-status').click()


def confirm_on_respondent_page(_):
    assert 'Respondents | Survey Data Collection' in browser.title

