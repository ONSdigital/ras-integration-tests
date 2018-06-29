from acceptance_tests.features.steps.authentication import signed_in_respondent
from config import Config

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_external
from controllers import messages_controller


def go_to():
    browser.visit(f"{Config.FRONTSTAGE_SERVICE}/secure-message/threads")


def go_to_surveys_todo():
    browser.visit(f"{Config.FRONTSTAGE_SERVICE}/surveys/todo")


def select_to_create_message():
    browser.find_by_id('create-message-link-1').click()


def get_page_title():
    return browser.title


def get_summary_length():
    return len(browser.find_by_id('message-summary-1'))


def get_message_body_summary():
    return browser.find_by_id('message-summary-1').text


def send_message_from_internal():
    messages_controller.create_message_internal_to_external('Message received from ONS', 'Message body')


def send_message_from_external():
    messages_controller.create_message_external_to_internal()


def send_message_from_external_with_body_over_80_characters():
    # Get authentication and navigate to correct page
    signed_in_respondent(())
    go_to_surveys_todo()
    select_to_create_message()

    # Create message
    create_message_external.enter_valid_subject('Long message')
    create_message_external.enter_valid_body_over_80_character_summary()

    # Send message
    create_message_external.send_message()


def get_no_messages_text():
    return browser.find_by_text('No new conversations')
