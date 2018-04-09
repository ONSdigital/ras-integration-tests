from acceptance_tests import browser
from config import Config


def get_conversation_messages():
    return browser.find_by_name('conversation-message')


def get_body_from_conversation_message(conversation_message):
    return conversation_message.find_by_name('conversation-message-body').value


def get_sent_date_from_conversation_message(conversation_message):
    return conversation_message.find_by_name('sm-sent-date').value


def get_sender_from_conversation_message(conversation_message):
    return conversation_message.find_by_name('sm-sender').value


def go_to_first_conversation_in_message_box():
    browser.visit(f"{Config.FRONTSTAGE_SERVICE}/secure-message/threads")
    browser.driver.find_element_by_id("open-conversation-link-1").click()


def get_first_conversation_in_message_box():
    go_to_first_conversation_in_message_box()
    return get_conversation_messages()
