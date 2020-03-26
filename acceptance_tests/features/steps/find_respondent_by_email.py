from behave import given, when, then

from acceptance_tests.features.pages import respondent
from controllers.party_controller import get_party_by_email


@given('the respondent account with an email has been created')
def create_respondent_account(context):
    respondent_party = get_party_by_email(context.respondent_email)

    assert respondent_party is not None, f'No respondent with email {context.respondent_email} exists'


@when('an internal user searches for respondent using their email address')
@given('the internal user has navigated to a respondents details page')
def go_to_respondent_detail_page(context):
    respondent.go_to_individual_respondent_page(context.respondent_id)


@then('the respondent details should be displayed')
def assert_respondent_details_displayed(context):
    respondent_details = respondent.get_respondent_details()

    assert context.respondent_email in respondent_details[
        'email'], "No respondent with email " + context.respondent_email


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
