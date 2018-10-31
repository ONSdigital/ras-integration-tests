from acceptance_tests import browser
from behave import given, then, when
import acceptance_tests.features.pages.view_and_reply_conversation_external as page_helpers
from acceptance_tests.features.pages.create_message_internal import get_first_flashed_message
from acceptance_tests.features.pages.external_conversation import go_to_closed
from acceptance_tests.features.pages.inbox_internal import go_to as go_to_internal_bricks_messages
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread as go_to_thread_internal
from acceptance_tests.features.pages.reply_to_message_internal import get_current_url
from acceptance_tests.features.pages.reply_to_message_internal import \
    reply_to_first_message_in_message_box as reply_to_last_message_internal
from acceptance_tests.features.steps.authentication import signed_in_internal, signed_in_respondent
from controllers.messages_controller import create_message_external_to_internal, \
    create_and_close_message_internal_to_external


@given('an external user has sent ONS a message')
def external_user_has_sent_ONS_a_message(context):
    create_message_external_to_internal(context, 'Message to ONS', 'Message body to ONS')


@when('an internal user responds')
def internal_user_replies_to_last_message(context):
    signed_in_internal(None)
    reply_to_last_message_internal()

    # sign in again as respondent
    signed_in_respondent(context)


@when('the user navigates to the external closed inbox messages')
def navigate_to_external_closed_messages(_):
    go_to_closed()


@then('the external user can see all messages in the conversation')
def external_user_can_see_all_messages_in_conversation(_):
    conversation = page_helpers.get_first_conversation_in_message_box()

    assert len(conversation) == 2

    original_message = page_helpers.get_body_from_conversation_message(conversation[0])
    internal_reply = page_helpers.get_body_from_conversation_message(conversation[1])

    assert 'Message body to ONS' == original_message
    assert 'Body of reply from ONS internal user' == internal_reply


@then('the external user can see the date and time for each message in the conversation')
def external_user_can_see_date_and_time_of_messages_in_conversation(_):
    conversation = page_helpers.get_first_conversation_in_message_box()

    original_message_sent_date = page_helpers.get_sent_date_from_conversation_message(conversation[0])
    internal_reply_sent_date = page_helpers.get_sent_date_from_conversation_message(conversation[1])

    assert 'Today at' in original_message_sent_date
    assert 'Today at' in internal_reply_sent_date


@then('the external user can see which messages have been sent by ONS and which ones they have sent')
def external_user_can_distinguish_sent_and_received_messages(_):
    conversation = page_helpers.get_first_conversation_in_message_box()

    original_message_sender = page_helpers.get_sender_from_conversation_message(conversation[0])
    internal_reply_sender = page_helpers.get_sender_from_conversation_message(conversation[1])

    assert internal_reply_sender != original_message_sender
    assert internal_reply_sender == 'ONS Business Surveys Team'


@then('they are taken to the latest message in that conversation (external)')
def external_user_is_anchored_to_latest_message_in_conversation(_):

    # Check url anchors to latest-message tag
    assert '#latest-message' in get_current_url()

    # Check there is only one latest message tag
    assert len(page_helpers.get_latest_message_by_tag()) == 1

    # Check the latest message tag is on the last message in the conversation
    assert len(page_helpers.get_latest_message_tag_from_latest_message()) == 1


@given('the external user has a conversation')
def external_user_has_a_conversation(context):
    create_message_external_to_internal(context, 'Message to ONS', 'Message body to ONS')
    signed_in_internal(None)
    reply_to_last_message_internal()
    signed_in_respondent(context)
    page_helpers.go_to_first_conversation_in_message_box()


@given('the external user has a closed conversation')
def external_user_has_a_closed_conversation(_):
    create_and_close_message_internal_to_external('Message to ONS', 'Message body to ONS')


@when('they view that conversation')
def external_user_views_conversation(_):
    page_helpers.go_to_first_conversation_in_message_box()


@when('they view the closed conversation')
def external_user_views_closed_conversation(_):
    page_helpers.go_to_first_closed_conversation_in_message_box()


@then('they are able to reply (external)')
@when('they reply in that conversation')
def external_user_able_to_reply_to_conversation(_):
    page_helpers.go_to_first_conversation_in_message_box()
    page_helpers.enter_text_in_conversation_reply('Reply body from respondent')
    page_helpers.click_reply_send_button()

    assert "Message sent." in get_first_flashed_message()


@when('they enter text into the body of their reply (external)')
def external_user_enters_text_in_reply(_):
    page_helpers.enter_text_in_conversation_reply('Reply body from respondent')


@then('they are able to reply to the conversation')
def external_user_able_to_reply_to_conversation_no_setup(_):
    page_helpers.click_reply_send_button()
    assert "Message sent." in get_first_flashed_message()


@then('the reply will be sent to the correct team')
def external_user_reply_sent_to_correct_team(_):
    signed_in_internal(None)
    go_to_internal_bricks_messages()
    go_to_thread_internal()
    latest_message_body = page_helpers.get_body_from_last_message()
    assert latest_message_body == 'Reply body from respondent'


@then('they are able able to enter up to and including 10,000 characters in the body of their reply')
def external_user_able_to_enter_body_up_to_correct_limit(_):
    page_helpers.go_to_first_conversation_in_message_box()

    # Check user can enter 10000 characters
    page_helpers.enter_text_in_conversation_reply_with_javascript('a'*9900)
    page_helpers.enter_text_in_conversation_reply('a' * 100)
    assert page_helpers.get_text_from_reply_text_area() == 'a' * 10000

    # Check user cannot enter more than 10000 characters
    page_helpers.enter_text_in_conversation_reply('a'*100)
    assert page_helpers.get_text_from_reply_text_area() == 'a' * 10000


@then('they are to be navigated back to the list of conversations')
def external_user_is_navigated_to_list_of_conversations(_):
    assert 'secure-message/threads' in get_current_url()


@then('they receive confirmation that the message has been sent (external)')
def external_user_receives_confirmation_that_message_has_been_sent(_):
    assert "Message sent." in get_first_flashed_message()


@then('they are informed that the conversation is closed')
def external_conversation_closed_message(_):
    assert browser.find_by_text('This conversation has now been closed. ')
    assert browser.driver.find_element_by_link_text('to do list')
    assert browser.driver.find_element_by_link_text('history')
