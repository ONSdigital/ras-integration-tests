import logging

from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal, create_message_external, surveys_todo
from acceptance_tests.features.pages.reporting_unit import click_data_panel
from acceptance_tests.features.steps.authentication import signed_in_respondent, signed_in_internal
from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def go_to_create_message():
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}'
                  "/reporting-units/49900000001")
    click_data_panel('Bricks')
    browser.find_by_id("create-message-button-1").click()
    assert "messages/create-message" in browser.url


def create_message_internal_to_external(subject='Subject', body='Body'):
    # Send a message from a respondent in the context of a Bricks survey
    # Note that external users may have to be signed in again after calling this function

    # Navigate to sent a message
    signed_in_internal(())
    go_to_create_message()

    # Create message
    create_message_internal.enter_text_in_message_subject(subject)
    create_message_internal.enter_text_in_message_body(body)

    # Send message
    create_message_internal.click_message_send_button()
    logger.debug("Message from internal to external created")


def create_message_external_to_internal(subject='Subject', body='Body'):
    # Send a message from a respondent in the context of a Bricks survey
    # Note that internal users may have to be signed in again after calling this function

    # Navigate to send a message
    signed_in_respondent(())
    surveys_todo.go_to()
    surveys_todo.select_to_create_message()

    # Create message
    create_message_external.enter_valid_subject(subject)
    create_message_external.enter_valid_body(body)

    # Send message
    create_message_external.send_message()
    logger.debug("Message from external to internal created")
