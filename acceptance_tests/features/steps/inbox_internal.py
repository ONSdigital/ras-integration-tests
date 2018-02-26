import time
from datetime import datetime

from behave import given, when, then

from acceptance_tests.features.pages import home, inbox
from common.respondent_details import RESPONDENT_DETAILS
from controllers import messages_controller


@given('the user has access to secure messaging')
def verify_messages_link_present(_):
    assert home.verify_messages_link_present()


@given('the user has got messages in their inbox')
def populate_database_with_messages(_):
    respondent_id = [RESPONDENT_DETAILS.get_respondent_id()]
    ru_id = RESPONDENT_DETAILS.get_ru_id()
    messages_controller.create_message(respondent_id, "test subject", "test body", ru_id)
    # 1 sec sleep so that there is a different timestamp on the message
    time.sleep(1)
    messages_controller.create_message(respondent_id, "test subject2", "test body2", ru_id)


@when('they navigate to the inbox messages')
def internal_user_views_messages(_):
    inbox.go_to()


@then('they are informed that there are no messages')
def informed_of_no_messages(_):
    assert inbox.get_no_messages_text().text == 'No new messages'


@then('they are able to view all received messages')
def test_presence_of_messages(_):
    assert len(inbox.get_messages()) > 0


@then('they are able to view the RU Ref, Subject, From, To, Date/Time for each message')
def test_inbox_headings(_):
    assert inbox.get_table_heading() == "RU_Ref Business name Subject From To Received"


@then('they are able to view all received messages in reverse chronological order/latest first')
def test_message_order(_):
    messages = inbox.get_messages()
    first_message_date = datetime.strptime(messages[0].get('received'), '%Y-%m-%d %H:%M:%S')
    second_message_date = datetime.strptime(messages[1].get('received'), '%Y-%m-%d %H:%M:%S')
    assert first_message_date > second_message_date
