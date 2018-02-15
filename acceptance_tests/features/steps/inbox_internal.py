from behave import given, when, then

from acceptance_tests.features.pages import home, inbox

@given('the user has access to secure messaging')
def verify_messages_link_present(_):
    assert home.verify_messages_link_present()

@when('they navigate to the inbox messages')
def internal_user_views_messages(_):
    inbox.go_to()

@then('they are able to view all received messages')
def should_be_able_to_see_messages(_):
    messages_list = inbox.get_messages()
    assert not messages_list

@then('they are informed that there are no messages')
def informed_of_no_messages(_):
    assert inbox.get_no_messages_text().first.text == 'No new messages'
