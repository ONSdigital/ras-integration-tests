from acceptance_tests import browser
from config import Config


def go_to_find_respondent():
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/respondents/')


def go_to_individual_respondent_page(id):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/respondents/respondent-details/{id}')


def search_respondent_by_email(email):
    browser.find_by_id('email_address').fill(email)
    browser.find_by_id('btn-search-respondent').click()


def no_results_found():
    return 'No results found' in browser.html


def get_respondent_details():
    respondent_details = {
        "email": browser.find_by_id('respondent-email'),
        "name": browser.find_by_id('respondent-name'),
        "telephone": browser.find_by_id('respondent-phone'),
        "account_status": browser.find_by_id('respondent-account-status')
    }
    return respondent_details


def not_found():
    return '0 respondents found' in browser.html


def click_edit_contact_details():
    browser.find_by_id('edit-contact-details').click()


def click_resend_verification_email():
    browser.find_by_id('resend-email-verification-btn').click()


def click_change_enrolment_status(_):
    browser.find_by_id('change-enrolment-status').click()


def confirm_on_respondent_page(_):
    assert 'Respondents | Survey Data Collection' in browser.title

