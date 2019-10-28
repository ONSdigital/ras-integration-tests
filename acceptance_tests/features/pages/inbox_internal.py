from acceptance_tests import browser
from common.browser_utilities import wait_for_url_matches
from config import Config


def go_to_using_context(context, conversation_tab='open'):
    tab = conversation_tab.replace(' ', '+')
    target_url = f"{Config.RESPONSE_OPERATIONS_UI}/messages/{context.short_name}?conversation_tab={tab}"
    browser.visit(target_url)
    wait_for_url_matches(target_url, timeout=3, retry=0.5, post_change_delay=0.1)


def go_to_select_survey():
    target_url = f"{Config.RESPONSE_OPERATIONS_UI}/messages/select-survey"
    browser.visit(target_url)
    wait_for_url_matches(target_url, timeout=3, retry=0.5, post_change_delay=0.1)


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
    return browser.find_by_text('No new conversations')


def get_no_closed_conversations_text():
    return browser.find_by_text('No closed conversations')


def get_no_my_conversations_text():
    return browser.find_by_text('There are currently no messages')


def get_dropdown_list():
    return browser.driver.find_element_by_id('survey-list')


def get_filter_page_title():
    return browser.find_by_text('Filter messages by survey')


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


def closed_tab_present():
    return browser.driver.find_element_by_link_text('Closed')
