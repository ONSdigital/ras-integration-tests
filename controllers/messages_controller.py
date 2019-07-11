import logging

from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal, create_message_external, inbox_internal, \
    surveys_todo
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread
from acceptance_tests.features.pages.reporting_unit import click_data_panel
from acceptance_tests.features.steps.authentication import signed_in_respondent, signed_in_internal
from acceptance_tests.features.pages.sign_out_internal import try_sign_out
from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def go_to_create_message(context):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/reporting-units/{context.short_name}')
    click_data_panel(context.short_name)
    browser.find_by_id("create-message-button-1").click()
    assert "messages/create-message" in browser.url


def create_message_internal_to_external(context, subject='Subject', body='Body'):
    # Send a message from a respondent in the context of a Bricks survey
    # Note that external users may have to be signed in again after calling this function

    # Navigate to sent a message
    try_sign_out()
    signed_in_internal(context)
    go_to_create_message(context)

    # Create message
    create_message_internal.enter_text_in_message_subject(subject)
    create_message_internal.enter_text_in_message_body(body)

    # Send message
    create_message_internal.click_message_send_button()
    logger.debug("Message from internal to external created")


def create_message_external_to_internal(context, subject='Subject', body='Body'):
    # Send a message from a respondent in the context of a Bricks survey
    # Note that internal users may have to be signed in again after calling this function

    # Navigate to send a message
    signed_in_respondent(context)
    surveys_todo.go_to()
    surveys_todo.select_to_create_message()

    # Create message
    create_message_external.enter_valid_subject(subject)
    create_message_external.enter_valid_body(body)

    # Send message
    create_message_external.send_message()
    logger.debug("Message from external to internal created")


def create_multiple_messages_external_to_internal(context, number_of_messages, subject='Subject', body='Body'):
    signed_in_respondent(context)

    for i in range(number_of_messages):
        surveys_todo.go_to()
        surveys_todo.select_to_create_message()

        create_message_external.enter_valid_subject(f"{subject}_{str(i)}")
        create_message_external.enter_valid_body(f"{body}_{str(i)}")

        create_message_external.send_message()


def create_and_close_message_internal_to_external(context, subject='Subject', body='Body'):
    create_message_internal_to_external(context, subject=subject, body=body)
    inbox_internal.go_to_using_context(context)
    go_to_thread()
    create_message_internal.click_close_conversation_button()
    create_message_internal.click_confirm_close_conversation_button()
