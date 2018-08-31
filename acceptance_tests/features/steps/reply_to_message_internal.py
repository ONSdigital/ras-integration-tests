from behave import given, when, then

from acceptance_tests.features.pages import create_message_internal
from acceptance_tests.features.pages import inbox_internal
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread
from acceptance_tests.features.pages.reply_to_message_internal import get_current_url
from acceptance_tests.features.steps.authentication import signed_in_internal
from controllers.messages_controller import create_message_external_to_internal


@given('the internal user has received a message')
def internal_user_receive_message(_):
    create_message_external_to_internal()

    # Sending external to internal may sign out the internal user
    signed_in_internal(None)


@when('they view the message')
def internal_user_can_view_message(_):
    inbox_internal.go_to()
    go_to_thread()


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
