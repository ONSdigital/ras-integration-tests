import logging

from structlog import wrap_logger

from acceptance_tests.features.pages import create_message_internal, create_message_external, surveys_todo
from acceptance_tests.features.steps.authentication import signed_in_respondent

logger = wrap_logger(logging.getLogger(__name__))


def create_message_internal_to_external(subject, body):

    # Navigate to sent a message
    create_message_internal.go_to()

    # Create message
    create_message_internal.enter_text_in_message_subject(subject)
    create_message_internal.enter_text_in_message_body(body)

    # Send message
    create_message_internal.click_message_send_button()
    logger.info("Message from internal to external created")


def create_message_external_to_internal():
    # Send a message from a respondent in the context of a Bricks survey
    # Note that internal users may have to be signed in again after calling this function

    # Navigate to send a message
    signed_in_respondent(())
    surveys_todo.go_to()
    surveys_todo.select_to_create_message()

    # Create message
    create_message_external.enter_valid_subject()
    create_message_external.enter_valid_body()

    # Send message
    create_message_external.send_message()
    logger.info("Message from external to internal created")
