from config import Config

from acceptance_tests import browser


def go_to():
    browser.visit(f"{Config.FRONTSTAGE_SERVICE}/secure-message/threads")


def get_page_title():
    return browser.title


def go_to_todo_and_click_send_message():
    browser.visit(f"{Config.FRONTSTAGE_SERVICE}/surveys/todo")
    browser.find_by_id('create-message-link-1').click()


def get_no_messages_text():
    return browser.find_by_text('No new messages')


