
import logging

from structlog import wrap_logger

from acceptance_tests.features.pages import create_message_internal

logger = wrap_logger(logging.getLogger(__name__))


def create_message(subject, body):
    create_message_internal.go_to()
    # create message
    create_message_internal.enter_text_in_message_subject(subject)
    create_message_internal.enter_text_in_message_body(body)
    # Send message
    create_message_internal.click_message_send_button()
    logger.info("Message created")
