from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_respondent
from common.respondent_utilities import register_respondent
from controllers.party_controller import get_party_by_email


def creating_unverified_account(username):
    email_in_use = get_party_by_email(username)
    if not email_in_use:
        register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                            username=username, ru_ref=49900000001, verified=False)


def respondent_enters_wrong_password(username):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(username)
    browser.driver.find_element_by_id('inputPassword').send_keys('wrong-password')
    browser.find_by_id('sign_in_button').click()


def locking_respondent_out(username):
    for i in range(0, 10):
        respondent_enters_wrong_password(username=username)


def get_lockout_message():
    return browser.find_by_text("You've tried to sign in a few times with the wrong details.")


def respondent_password_reset_complete():
    return browser.find_by_text('Your password has been changed')
