from behave import given, when, then

from acceptance_tests.features.pages import browser, inbox_internal
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread, count_thread_message, \
    is_conversation_with_sent_and_received_messages, view_full_conversation_date_time_msg_details, \
    view_last_anchored_message
from controllers.messages_controller import create_message_internal_to_external


@given('An internal user has conversations in their inbox')
def populate_database_with_messages(context):
    create_message_internal_to_external(context, "This is the subject of the message",
                                        "This is the body of the message")
    assert len(inbox_internal.get_messages()) > 0


@when('The internal user selects a conversation')
def select_thread(_):
    go_to_thread()


@then('the internal user can see all messages in the conversation')
def view_all_thread_message(_):
    assert count_thread_message() == 1


@then('The internal user can see which messages have been sent by ONS users and which are an external users messages')
def identify_message_sender(_):
    assert(is_conversation_with_sent_and_received_messages())


@then('The internal user can see the date and time for each message in the conversation')
def check_date_time(_):
    assert (view_full_conversation_date_time_msg_details() == 1)


@then('They are taken to the latest message in that conversation')
def check_page_takes_to_anchor_on_load(_):
    assert (view_last_anchored_message())


@then('They can see mark as unread')
def check_mark_as_unread_available(_):
    assert browser.find_by_id('sm-mark-as-unread')


@then('They cannot see mark as unread')
def check_mark_as_unread_unavailable(_):
    assert not browser.find_by_id('sm-mark-as-unread')


@when('they select mark unread')
def select_mark_unread(context):
    browser.click_link_by_id('sm-mark-as-unread')


@then("they are taken to conversation view")
def user_is_navigated_to_conversation(_):
    assert 'messages/' in browser.url


@then('the expected message is displayed')
def message_marked_unread_message_displayed(context):
    assert browser.find_by_id('flashed-message-1')
    flash_message = browser.find_by_id('flashed-message-1')
    assert "marked unread" in flash_message.text
