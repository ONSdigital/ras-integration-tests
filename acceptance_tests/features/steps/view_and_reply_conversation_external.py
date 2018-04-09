from behave import given, then, when

from controllers.messages_controller import create_message_external_to_internal
from acceptance_tests.features.pages.inbox_internal import go_to as go_to_internal_inbox
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread as go_to_first_thread
from acceptance_tests.features.steps.authentication import signed_in_internal, signed_in_respondent
import acceptance_tests.features.pages.view_and_reply_conversation_external as page_helpers


@given('an external user has sent ONS a message')
def external_user_has_sent_ONS_a_message(_):
    create_message_external_to_internal('Message to ONS', 'Message body to ONS')


@when('an internal user responds')
def internal_user_replies_to_last_message(_):
    signed_in_internal()
    go_to_internal_inbox()
    go_to_first_thread()
    # TODO reply from internal

    # sign in again as respondent
    signed_in_respondent()


@then('the external user can see all messages in the conversation')
def external_user_can_see_all_messages_in_conversation(_):
    # TODO go to external conversation

    conversation = page_helpers.get_conversation_messages()
    assert len(conversation) == 2

    original_message = page_helpers.get_body_from_conversation_message(conversation[0])
    internal_reply = page_helpers.get_body_from_conversation_message(conversation[1])

    assert 'Message body to ONS' == original_message
    assert 'Respondent reply' == internal_reply


@then('the external user can see the date and time for each message in the conversation')
def external_user_can_see_date_and_time_of_messages_in_conversation(_):
    pass


@then('the external user can see which messages have been sent by ONS and which ones they have sent')
def external_user_can_distinguish_sent_and_received_messages(_):
    pass


@given('the external user has a conversation')
def external_user_has_a_conversation(_):
    pass


@when('they view that conversation')
def external_user_views_conversation(_):
    pass


@then('they are able to reply')
@then('they are able to reply to the conversation')
@when('they reply in that conversation')
def external_user_able_to_reply_to_conversation(_):
    pass


@then('the reply will be sent to the correct team')
def external_user_reply_sent_to_correct_team(_):
    pass


@then('they are able able to enter up to and including 10,000 characters in the body of their reply')
def external_user_able_to_enter_body_up_to_correct_limit(_):
    pass


@when('they enter text into the body of their reply')
def external_user_enters_text_in_reply_body(_):
    pass


@then('they are to be navigated back to the list of conversations')
def external_user_is_navigated_to_list_of_conversations(_):
    pass


@then('they receive confirmation that the message has been sent')
def external_user_receives_confirmation_that_message_has_been_sent(_):
    pass
