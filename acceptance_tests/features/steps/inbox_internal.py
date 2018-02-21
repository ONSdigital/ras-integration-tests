from behave import given, when, then

from acceptance_tests.features.pages import home, inbox
from controllers import database_controller

@given('the user has access to secure messaging')
def verify_messages_link_present(_):
    assert home.verify_messages_link_present()

@given('the secure message database is populated with messages')
def populate_database_with_messages(_):
    database_controller.create_secure_messages()

@when('they navigate to the inbox messages')
def internal_user_views_messages(_):
    inbox.go_to()

@then('they are informed that there are no messages')
def informed_of_no_messages(_):
    assert inbox.get_no_messages_text().first.text == 'No new messages'

@then('they are able to view all received messages')
def test_presence_of_messages(_):
    assert len(inbox.get_messages()) > 0
