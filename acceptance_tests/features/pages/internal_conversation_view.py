
from config import Config

from acceptance_tests import browser


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/messages")


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
    """
    The anchor should be present just in the last visible message in th ebottom fo the page. The anchor
    is a upper level comparing the message that can be of 2 kinds , internal or external, that s why i m trying to
    get any last message that starts with sm-from-  (ons/respondent)
    :return the message found.
    """
    re1 = '(sm)'  # Word 1
    re2 = '(-)'  # Any Single Character 1
    re3 = '(from)'  # Word 2
    re4 = '(-)'  # Any Single Character 2
    re5 = '((?:[a-z][a-z0-9_]*))'  # Variable Name 1
    re6 = '(-)'  # Any Single Character 3
    re7 = '(\\d+)'  # Integer Number 1

    anchor = browser.find_by_id('latest-message')
    return anchor.find_by_xpath(re1 + re2 + re3 + re4 + re5 + re6 + re7)
