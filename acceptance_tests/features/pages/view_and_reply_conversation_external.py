from acceptance_tests import browser


def get_conversation_messages():
    return browser.find_by_name('conversation-message')


def get_body_from_conversation_message(conversation_message):
    return conversation_message.find_by_name('message_body').value
