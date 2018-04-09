from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_external, external_conversation


@given('the external user has conversations in their list')
def external_user_has_two_conversations(_):
    external_conversation.go_to_todo_and_click_send_message()
    create_message_external.enter_valid_subject()
    create_message_external.enter_invalid_length_body()
    create_message_external.send_message()

    external_conversation.go_to_todo_and_click_send_message()
    create_message_external.enter_valid_subject()
    create_message_external.enter_invalid_length_body()
    create_message_external.send_message()


@given('the external user has no conversations to view')
def no_conversations_to_view(_):
    pass


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


@then('they are able to preview the first 100 characters (respecting word boundaries) of the latest message in the conversation')  # NOQA
def preview_summary_of_conversation(_):
    pass


@then('the user will be able to view the conversation subject and the date and time the latest message was received')
def view_date_and_time_of_conversation(_):
    pass


@then('they are able to distinguish that the external message is unread')
def external_message_is_unread(_):
    pass
