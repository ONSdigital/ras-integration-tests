import time
from datetime import datetime

from behave import given, when, then

from acceptance_tests.features.pages import home, inbox
from acceptance_tests.features.pages.inbox import go_to_thread, count_thread_message, \
    is_conversation_whit_sent_and_received_messages
from common.respondent_details import RESPONDENT_DETAILS
from controllers import messages_controller, database_controller


@given('the user has access to secure messaging')
def verify_messages_link_present(_):
    assert home.verify_messages_link_present()


@given('the user has got messages in his inbox')
def populate_database_with_messages(_):
    messages_controller.create_thread()
    inbox.go_to()


@when('The internal user selects a conversation')
def select_thread():
    go_to_thread()


@given('An internal user has conversations in their inbox')
def test_presence_of_messages(_):
    assert len(inbox.get_messages()) > 0


@then('the internal user can see all messages in the conversation')
def view_all_thread_message():
    assert len(count_thread_message()) == 3

@then('The internal user can see the date and time for each message in the conversation')
def viw_conversation_msg_date_time():


@then('The internal user can see which messages have been sent by ONS users and which are an external users messages')
def identify_message_sender():
    assert(is_conversation_whit_sent_and_received_messages())

@then('They are taken to the latest message in that conversation')
    #def isTheLastMessage
