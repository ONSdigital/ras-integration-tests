from behave import given, when, then

from acceptance_tests.features.pages import respondent
from controllers.party_controller import get_party_by_email, change_respondent_status


@given('the respondent account with email "{email_address}" has been created')
def create_respondent_account(_, email_address):
    respondent_party = get_party_by_email(email_address)

    assert respondent_party is not None
    assert 'example@example.com' in respondent_party['emailAddress']


@given('the respondent email "{email_address}" is verified')
def verify_respondent_account(_, email_address):
    respondent_party = get_party_by_email(email_address)

    change_respondent_status(respondent_party['id'], "ACTIVE")


@when('an internal user searches for respondent using their email address "{email_address}"')
def search_respondent_by_email(_, email_address):
    respondent.go_to_find_respondent()
    respondent.search_respondent_by_email(email_address)


@then('the respondent details should be displayed')
def assert_respondent_details_displayed(_):
    respondent_details = respondent.get_respondent_details()

    assert 'example@example.com' in respondent_details['email']


@then('the internal user is given a message of no respondent for email')
def assert_no_respondent_displayed(_):
    page_src = respondent.find_no_respondent_msg()
    assert 'No Respondent found.' in page_src


@given('the respondent account with email "{email_address}" has not been created')
def check_no_respondent(_, email_address):
    respondent_party = get_party_by_email(email_address)

    assert respondent_party is None


@when('the internal user searches for the respondent using the email "{email_address}"')
def check_for_dummy_respondent(_, email_address):
    respondent.go_to_find_respondent()
    respondent.search_respondent_by_email(email_address)
