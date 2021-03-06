from acceptance_tests import browser
from acceptance_tests.features.pages import inbox_internal, create_message_internal
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread


def get_current_url():
    return browser.url


def reply_to_first_message_in_message_box(context):
    inbox_internal.go_to_using_context(context, 'open')
    go_to_thread()
    create_message_internal.enter_text_in_message_body('Body of reply from ONS internal user')
    create_message_internal.click_message_send_button()
