import time
from datetime import datetime

from behave import given, when, then

from acceptance_tests.features.pages import home, inbox_internal
from controllers import messages_controller, database_controller


@given('the user has access to secure messaging')
def verify_messages_link_present(_):
    assert home.verify_messages_link_present()


@given('the user has got messages in their inbox')
def populate_database_with_messages(_):

    messages_controller.create_message("This is the subject of the message", "This is the body of the message")
    # 1 sec sleep so that there is a different timestamp on the message
    time.sleep(2)
    messages_controller.create_message("This is the subject of the message", "This is the body of the message")
    inbox_internal.go_to()


@given('the user has no messages in their inbox')
def user_has_no_messages_in_inbox(_):
    database_controller.reset_secure_message_database()


@when('they navigate to the inbox messages')
def internal_user_views_messages(_):
    inbox_internal.go_to()


@then('they are informed that there are no messages')
def informed_of_no_messages(_):
    assert inbox_internal.get_no_messages_text().text == 'No new messages'


@then('they are able to view all received messages')
def test_presence_of_messages(_):
    assert len(inbox_internal.get_messages()) > 0


@then('they are able to view the RU Ref, Subject, From, To, Date and time for each message')
def test_inbox_headings(_):
    assert inbox_internal.get_table_heading() == "RU Ref Business name Subject From To Date and time"


@then('they are able to view all received messages in reverse chronological order/latest first')
def test_message_order(_):
    messages = inbox_internal.get_messages()
    first_message_date = datetime.strptime(messages[0].get('received').split(' ')[2], '%H:%M')
    second_message_date = datetime.strptime(messages[1].get('received').split(' ')[2], '%H:%M')
    assert first_message_date >= second_message_date


@when('they navigate to the select survey page')
def test_view_select_survey_page(_):
    inbox_internal.go_to_select_survey()


@then('they are able to view a list of filter options')
def test_select_survey_page_view(_):
    assert inbox_internal.get_radio_button_for_survey('ASHE')
    assert inbox_internal.get_radio_button_for_survey('Bricks')
