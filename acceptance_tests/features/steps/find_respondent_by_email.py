from behave import given, when, then

from acceptance_tests.features.pages import respondent
from controllers.party_controller import get_party_by_email


@given('the respondent account with an email has been created')
def create_respondent_account(context):
    respondent_party = get_party_by_email(context.user_name)

    assert respondent_party is not None, "No respondent with email example@example.com exists"


@when('an internal user searches for respondent using their email address')
def search_respondent_by_email(context):
    respondent.go_to_find_respondent()
    respondent.search_respondent_by_email(context.user_name)


@then('the respondent details should be displayed')
def assert_respondent_details_displayed(context):
    respondent_details = respondent.get_respondent_details()

    assert context.user_name in respondent_details['email'], "No respondent with email " + context.user_name


@then('the internal user is given a message of no respondent for email')
def assert_no_respondent_displayed(_):
    assert respondent.not_found()


@given('the respondent account with email "{email_address}" has not been created')
def check_no_respondent(_, email_address):
    respondent_party = get_party_by_email(email_address)

    assert respondent_party is None, "Respondent with email " + email_address + " should not exist."


@when('the internal user searches for the respondent using the email "{email_address}"')
def check_for_dummy_respondent(_, email_address):
    respondent.go_to_find_respondent()
    respondent.search_respondent_by_email(email_address)
