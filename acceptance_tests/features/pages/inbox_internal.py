from config import Config

from acceptance_tests import browser


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages/Bricks")


def go_to_select_survey():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages/select-survey")


def get_page_title():
    return browser.title


def get_messages():
    messages = []
    table = browser.find_by_id('tbl-messages')
    rows = table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        messages.append({
            'ru_ref': row.find_by_name('tbl-messages-RU_Ref').value,
            'business_name': row.find_by_name('tbl-messages-business').value,
            'subject': row.find_by_name('tbl-messages-subject').value,
            'from': row.find_by_name('tbl-messages-from').value,
            'to': row.find_by_name('tbl-messages-to').value,
            'received': row.find_by_name('tbl-messages-received').value
        })
    return messages


def get_table_heading():
    table = browser.find_by_id('tbl-messages')
    headings = table.find_by_tag('thead').find_by_tag('tr')
    return headings[0].value


def get_no_messages_text():
    return browser.find_by_text('No new messages')


def get_radio_button_for_survey(survey):
    return browser.find_by_id(survey)


def get_unread_messages():
    return browser.find_by_name('message-unread')


def get_pagination_previous_link():
    return browser.driver.find_element_by_class_name('previous')


def get_pagination():
    return browser.driver.find_element_by_class_name('pagination')


def get_pagination_next_link():
    return browser.driver.find_element_by_class_name('next')


def get_message_link_index(number_of_messages):
    return browser.find_by_id(f"message-link-{number_of_messages}")
