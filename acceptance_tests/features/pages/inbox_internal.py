from acceptance_tests import browser
from acceptance_tests.features.steps.sign_out_internal import sign_out
from config import Config


def go_to(context):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages/{context.short_name}")


def go_to_closed():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages/Bricks?is_closed=true")


# todo delete above 2 methods when all tests use 2 below
def go_to_using_context(context):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages/{context.short_name}")


def go_to_closed_using_context(context):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages/{context.short_name}?is_closed=true")


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
    return browser.find_by_text('No new conversations')


def get_no_closed_conversations_text():
    return browser.find_by_text('No closed conversations')


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


def after_scenario_cleanup(_):
    # Sign out Internal user if possible
    if browser.find_by_id('sign-out-btn'):
        sign_out(_)
