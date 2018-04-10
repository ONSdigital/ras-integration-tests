from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import external_conversation


@given('the external user has conversations in their list')
def external_user_has_two_conversations(_):
    external_conversation.send_message_from_external()
    external_conversation.send_message_from_internal()


@given('the external user has no conversations to view')
def no_conversations_to_view(_):
    pass


@given('they receive a message body with over 80 characters')
def external_user_sent_message_with_over_80_characters(_):
    external_conversation.send_message_from_external_with_body_over_80_characters()


@when('they navigate to the external inbox messages')
def go_to_messages_box(_):
    external_conversation.go_to()


@then('they are able to view a list of external conversations')
def test_conversation_available(_):
    assert external_conversation.get_page_title() == 'Messages - ONS Business Surveys'
    assert browser.find_by_id('message-link-1')
    assert browser.find_by_id('message-link-2')


@then('they are informed that there are no external conversations')
def informed_of_no_messages(_):
    assert external_conversation.get_no_messages_text().text == 'No new messages'


@then('they are able to preview the first 80 characters (respecting word boundaries) of the latest message in the conversation')  # NOQA
def preview_summary_of_conversation(_):
    assert external_conversation.get_summary_length() < 80
    assert external_conversation.get_endswith_ellipsis()[-3:] == '...'


@then('the user will be able to view the conversation subject and the date and time the latest message was received')
def view_date_and_time_of_conversation(_):
    assert external_conversation.get_datetime() == 'Today'


@then('they are able to distinguish that the external message is unread')
def external_message_is_unread(_):
    assert browser.find_by_id('message-list-unread')
    assert browser.is_text_present('(New)')
