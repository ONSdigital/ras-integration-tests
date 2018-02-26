
from datetime import datetime
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


def are_headings_correct():
    table = browser.find_by_id('tbl-messages')
    headings = table.find_by_tag('thead').find_by_tag('tr')
    return headings[0].value == "RU_Ref Business name Subject From To Received"


def are_messages_in_reverse_chronological_order():
    messages = []
    table = browser.find_by_id('tbl-messages')
    rows = table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        date = row.find_by_name('tbl-messages-received').value
        dateobj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        messages.append(dateobj)

    # Dates are read from top to bottom so the first element will always be at the top.
    # Both elements are datetime objects which you can do simple comparisions on to
    # see which is the greater (most recent) of the 2 dates.
    return messages[0] > messages[1]


def get_no_messages_text():
    return browser.find_by_text('No new messages')
