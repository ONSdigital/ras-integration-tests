import re

from config import Config

from acceptance_tests import browser


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages")


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


def go_to_thread():
    thread_subject = browser.find_by_id('message-link-1')
    browser.click_link_by_id(thread_subject)


def count_thread_message():
    internals = browser.find_by_name('sm-from-ons')
    external = browser.find_by_name('sm-from-respondent')
    return len(internals + external)


def is_conversation_whit_sent_and_received_messages():
    internals = browser.find_by_name('sm-from-ons')
    external = browser.find_by_name('sm-from-respondent')

    return len(internals) == 2 and len(external) == 1


def view_full_conversation_date_time_msg_details():

    internals = browser.find_by_name('sm-from-ons')
    externals = browser.find_by_name('sm-from-respondent')

    count_internals = int(internals.find_by_id('sm-sent-date-1')) + int(internals.find_by_id('sm-sent-date-3'))
    count_externals = int(externals.find_by_id('sm-sent-date-1'))

    return count_externals + count_internals


def view_last_anchored_message():

    re1 = '(sm)'  # Word 1
    re2 = '(-)'  # Any Single Character 1
    re3 = '(from)'  # Word 2
    re4 = '(-)'  # Any Single Character 2
    re5 = '((?:[a-z][a-z0-9_]*))'  # Variable Name 1
    re6 = '(-)'  # Any Single Character 3
    re7 = '(\\d+)'  # Integer Number 1

    anchor = browser.find_by_id('latest-message')
    last_message = anchor.find_by_xpath(re1 + re2 + re3 + re4 + re5 + re6 + re7)
