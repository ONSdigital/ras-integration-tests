from behave import given, when, then

from acceptance_tests.features.pages import respondent
from controllers.party_controller import get_party_by_email, change_respondent_status


@given('the respondent account with email example@example.com has been created')
def create_respondent_account(_):
    respondent_party = get_party_by_email('example@example.com')

    assert respondent_party is not None
    assert 'example@example.com' in respondent_party['emailAddress']


@given('the respondent email is verified')
def verify_respondent_account(_):
    respondent_party = get_party_by_email('example@example.com')

    change_respondent_status(respondent_party['id'], "ACTIVE")


@when('an internal user searches for respondent using their email address')
def search_respondent_by_email(_):
    respondent.go_to_find_respondent()
    respondent.search_respondent_by_email('example@example.com')


@then('the respondent details should be displayed')
def assert_respondent_details_displayed(_):
    respondent_details = respondent.get_respondent_details()

    assert 'Jacky Turner' in respondent_details['name']


@then('the internal user is given a message of no respondent for email')
def assert_no_respondent_displayed(_):
    respondent.find_no_respondent_msg()


@given('the respondent account with email test@test.com has not been created')
def check_no_respondent(_):
    respondent_party = get_party_by_email('test@test.com')

    assert respondent_party is None


@when('the internal user searches for the respondent using the email test@test.com')
def check_for_dummy_respondent(_):
    respondent.go_to_find_respondent()
    respondent.search_respondent_by_email('test@test.com')
