from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import surveys_todo


@given('the respondent is on their todo list')
@when('the respondent navigates to their surveys todo list')
def surveys_todo_list(context):
    surveys_todo.go_to()


@then('the respondent is able to send a message')
def able_to_send_message_for_survey_ru(context):
    browser.find_by_id('create-message-link-1')


@given('the respondent chooses to send a message to ONS')
@given('the respondent is sending a message in relation to bricks')
@when('the respondent chooses to send a message for a specific RU and survey')
def select_create_message(context):
    surveys_todo_list(context)
    browser.find_by_id('create-message-link-1').click()


@then('the respondent is navigated to the create message page')
def assert_create_message_page(context):
    browser.find_by_id('secure-message-subject')


@when('the respondent enters a valid message')
def enter_valid_message(context):
    browser.driver.find_element_by_id('secure-message-subject').send_keys('123')
    browser.driver.find_element_by_id('secure-message-body').send_keys('345')


@then('the message will be sent to the internal Bricks mailbox')
def message_sent_to_bricks_workgroup(context):
    current_url = browser.driver.current_url
    assert 'survey=cb8accda-6118-4d3b-85a3-149e28960c54' in current_url


@when('the respondent enters more than 96 characters in the subject field')
def subject_field_too_long(context):
    browser.driver.find_element_by_id('secure-message-subject').send_keys('x' * 98)
    browser.driver.find_element_by_id('secure-message-body').send_keys('y' * 200)


@when('chooses to send the message')
@when('the message is sent')
@when('selects to send message')
def click_send_message_btn(context):
    browser.find_by_id('send-message-btn').click()


@then('an error message appears specifying subject too long')
def check_for_error_subject_too_long(context):
    browser.driver.find_element_by_link_text('Subject field length must not be greater than 100')


@when('the respondent enters more than 10000 characters in the body field')
def body_too_long(context):
    browser.driver.find_element_by_id('secure-message-subject').send_keys('x' * 50)
    browser.driver.find_element_by_id('secure-message-body').send_keys('y' * 11000)


@then('an error message appears specifying body too long')
def check_for_body_too_long_error(context):
    browser.driver.find_element_by_link_text('Body field length must not be greater than 10000')


@when('the respondent tries to send the message without populating the body and subject fields')
def empty_subject_and_body_fields(context):
    browser.driver.find_element_by_id('secure-message-subject').clear()
    browser.driver.find_element_by_id('secure-message-body').clear()
    browser.find_by_id('send-message-btn').click()


@then('an error message appears specifying body and subject fields are required')
def error_require_body_and_subject(context):
    browser.driver.find_element_by_link_text('Please enter a subject')
    browser.driver.find_element_by_link_text('Please enter a message')


@then('the respondent is navigated to their inbox')
def navigated_to_inbox(context):
    browser.driver.find_element_by_css_selector("#inbox-list.navigation-tabs.navigation-tabs--pills > .navigation-tabs__item.navigation-tabs__item--active > .navigation-tabs__tab")  # NOQA


@then('the respondent is navigated to their inbox and notified message sent successfully')
def navigated_to_inbox_show_message_sent_notif(context):
    browser.driver.find_element_by_css_selector("#inbox-list.navigation-tabs.navigation-tabs--pills > .navigation-tabs__item.navigation-tabs__item--active > .navigation-tabs__tab")  # NOQA
    browser.driver.find_element_by_id("message-success-notif")


@when('the respondent populates the body field but not the subject')
def populate_body_not_subject(context):
    browser.driver.find_element_by_id('secure-message-body').send_keys('123')


@then('an error message appears specifying subject must be populated')
def assert_error_no_subject(context):
    browser.driver.find_element_by_link_text('Please enter a subject')


@when('the respondent populates the subject field but not the body field')
def populate_subject_no_body(context):
    browser.driver.find_element_by_id('secure-message-subject').send_keys('456')


@then('an error message appears notifying the respondent a body must be supplied')
def assert_error_no_body(context):
    browser.driver.find_element_by_link_text('Please enter a message')
