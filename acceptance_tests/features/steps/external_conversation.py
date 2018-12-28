from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal, external_conversation, inbox_internal, \
    internal_conversation_view
from controllers.messages_controller import create_and_close_message_internal_to_external


@given('the external user has access to secure messaging')
def messages_tab_is_present(_):
    assert browser.find_by_id('SURVEY_MESSAGES_TAB')


@given('the external user has conversations in their list')
def external_user_has_two_conversations(context):
    external_conversation.send_message_from_external(context)
    external_conversation.send_message_from_internal(context)


@given('the external user has no conversations to view')
def no_conversations_to_view(_):
    pass


@given('they receive a message body with over 80 characters')
def external_user_sent_message_with_over_80_characters(context):
    external_conversation.send_message_from_external_with_body_over_80_characters(context)


@given('a closed conversation has been reopened')
def close_and_reopen_a_conversation(context):
    create_and_close_message_internal_to_external(context, 'Message to ONS', 'Message body to ONS')
    inbox_internal.go_to_closed_using_context(context)
    internal_conversation_view.go_to_thread()
    create_message_internal.click_reopen_conversation_button()


@when('the respondent navigates to their inbox')
@given("the respondent navigates to their inbox")
def go_to_messages_box(_):
    external_conversation.go_to()


@when('they navigate to the external closed inbox messages')
def go_to_closed_messages_box(_):
    external_conversation.go_to_closed()


@when('they click the Messages tab')
def select_messages_tab(_):
    external_conversation.go_to_messages_tab()


@then('they are able to view a list of external conversations')
def test_conversation_available(_):
    assert external_conversation.get_page_title() == 'Messages - ONS Business Surveys'
    assert browser.find_by_id('message-link-1')
    assert browser.find_by_id('message-link-2')


@then('they are informed that there are no external conversations')
def informed_of_no_open_messages(_):
    assert external_conversation.get_no_messages_text()


@then('they are informed that there are no external closed conversations')
def informed_of_no_closed_messages(_):
    assert external_conversation.get_no_closed_messages_text()


@then('they are able to preview the first 80 characters (respecting word boundaries) of the latest message in the conversation')  # NOQA
def preview_summary_of_conversation(_):
    assert external_conversation.get_summary_length() < 80
    assert external_conversation.get_message_body_summary()[-3:] == '...'


@then('the user will be able to view the conversation subject and the date and time the latest message was received')
def view_date_and_time_of_conversation(_):
    assert browser.find_link_by_text('Message received from ONS')
    assert browser.is_text_present('Today at')


@then('they are able to distinguish that the external message is unread')
def external_message_is_unread(_):
    assert browser.find_by_id('message-list-unread')
    assert browser.is_text_present('(New)')


@then('the external user can see the closed tab')
def closed_tab_is_visible(_):
    assert external_conversation.closed_tab_present()


@then('they are taken to their open conversations')
def open_conversations_are_visible(_):
    assert 'secure-message/threads' in browser.url
    assert 'is_closed=true' not in browser.url


@then('they are able to view the external conversation')
def message_present_in_inbox(_):
    assert browser.find_by_id('message-link-1')
