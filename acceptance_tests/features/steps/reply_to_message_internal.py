from acceptance_tests import browser
from behave import given, when, then
from datetime import datetime

from acceptance_tests.features.pages import create_message_internal
from acceptance_tests.features.pages import inbox_internal
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread
from acceptance_tests.features.pages.reply_to_message_internal import get_current_url
from acceptance_tests.features.steps.authentication import signed_in_internal
from controllers.messages_controller import create_message_external_to_internal, \
    create_and_close_message_internal_to_external


@given('the internal user has received a message')
def internal_user_receive_message(context):
    create_message_external_to_internal(context)

    # Sending external to internal may sign out the internal user
    signed_in_internal(None)


@given('the internal user has a conversation in their inbox')
def create_conversation_internal(context):
    create_message_external_to_internal(context)
    signed_in_internal(None)
    inbox_internal.go_to()
    go_to_thread()
    create_message_internal.enter_text_in_message_body('Body')
    create_message_internal.click_message_send_button()


@given('the internal user has a closed conversation in their inbox')
def create_and_close_conversation(_):
    create_and_close_message_internal_to_external()


@when('they view the message')
def internal_user_can_view_open_message(_):
    inbox_internal.go_to()
    go_to_thread()


@when('they view the closed message')
def internal_user_can_view_closed_message(_):
    inbox_internal.go_to_closed()
    go_to_thread()


@when('they close the conversation')
def close_a_conversation(_):
    create_message_internal.click_close_conversation_button()
    create_message_internal.click_confirm_close_conversation_button()


@when('they reopen the conversation')
def reopen_a_conversation(_):
    create_message_internal.click_reopen_conversation_button()


@when('they reply to the message')
@then('they are able to reply')
def internal_user_can_reply(_):
    create_message_internal.enter_text_in_message_body('Body')
    create_message_internal.click_message_send_button()
    assert 'Message sent' in create_message_internal.get_first_flashed_message()


@then('they are to be navigated to the inbox of messages')
def internal_user_navigated_to_inbox(_):
    assert '/messages/Bricks' in get_current_url()


@then('they receive confirmation that the message has been sent')
def internal_user_receives_confirmation(_):
    assert 'Message sent' in create_message_internal.get_first_flashed_message()


@then('they receive confirmation that the conversation is closed')
def internal_user_informed_that_conversation_is_closed(_):
    assert 'Conversation closed.' in create_message_internal.get_first_flashed_message()


@then('the conversation appears in their closed list')
def message_in_closed_list(_):
    inbox_internal.go_to_closed()
    assert len(inbox_internal.get_messages()) > 0


@then('the conversation is not present in their closed list')
def no_messages_in_closed_list(_):
    inbox_internal.go_to_closed()
    assert inbox_internal.get_no_closed_conversations_text()


@then('they receive confirmation that the conversation has been reopened')
def internal_user_informed_that_conversation_has_been_reopened(_):
    assert 'Conversation re-opened.' in create_message_internal.get_first_flashed_message()


@then('the conversation is present in their open list')
def conversation_in_open_list(_):
    inbox_internal.go_to()
    assert len(inbox_internal.get_messages()) > 0


@then('they are able to see the messages in the conversation in chronological order')
def messages_in_chronological_order(_):
    first_message_date = datetime.strptime(browser.find_by_id('sm-sent-date-1').value.split(' ')[2], '%H:%M')
    second_message_date = datetime.strptime(browser.find_by_id('sm-sent-date-2').value.split(' ')[2], '%H:%M')
    assert first_message_date <= second_message_date
