from behave import given, when, then

from acceptance_tests.features.pages.notifying_respondent_to_verify_email_address import enter_credentials, \
    log_in_respondent, get_verification_message, click_verification_link, get_verification_resend_message
from config import Config
from controllers.party_controller import reset_password


@given('an external user with unverified account tried to sign into their account')
def enter_respondent_credentials(_):
    enter_credentials(username='unverified@test.com', password=Config.RESPONDENT_PASSWORD)


@when('they enter correct credentials')
def log_in_attempt(_):
    log_in_respondent(_)


@then('they are shown on-screen notification to check their email')
def verification_page(_):
    assert get_verification_message(_)


@then('they are shown on-screen notification to request another verification link')
def verification_link(_):
    click_verification_link(_)
    assert get_verification_resend_message(_)


