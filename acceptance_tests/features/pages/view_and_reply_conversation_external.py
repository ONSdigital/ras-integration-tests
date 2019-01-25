from acceptance_tests import browser
from common.browser_utilities import wait_for_element_by_id
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
    wait_for_element_by_id(element_id="open-conversation-link-1", timeout=5, retry=1)
    browser.driver.find_element_by_id("open-conversation-link-1").click()


def go_to_first_closed_conversation_in_message_box():
    browser.visit(f"{Config.FRONTSTAGE_SERVICE}/secure-message/threads?is_closed=true")
    browser.driver.find_element_by_id("message-link-1").click()


def get_first_conversation_in_message_box():
    go_to_first_conversation_in_message_box()
    return get_conversation_messages()


def enter_text_in_conversation_reply(text):
    browser.driver.find_element_by_id("secure-message-body").send_keys(text)


def enter_text_in_conversation_reply_with_javascript(text):
    browser.execute_script(f'document.getElementById("secure-message-body").value="{text}";')


def get_text_from_reply_text_area():
    return browser.find_by_id("secure-message-body").value


def click_reply_send_button():
    browser.driver.find_element_by_id("send_message_button").click()


def get_latest_message_by_tag():
    return browser.find_by_id("latest-message")


def get_last_message_in_conversation():
    return get_conversation_messages()[-1]


def get_latest_message_tag_from_latest_message():
    return get_last_message_in_conversation().find_by_id("latest-message")


def get_body_from_last_message():
    return browser.find_by_name("conversation-message-body")[-1].value
