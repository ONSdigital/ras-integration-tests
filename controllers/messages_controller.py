
import logging

from structlog import wrap_logger

from acceptance_tests.features.pages import create_message_internal

logger = wrap_logger(logging.getLogger(__name__))


def create_message():
    create_message_internal.go_to()
    # create message
    create_message_internal.enter_text_in_message_subject("This is the subject of the message")
    create_message_internal.enter_text_in_message_body('This is the body of the message')
    # Send message
    create_message_internal.click_message_send_button()
    logger.info("Message created")
