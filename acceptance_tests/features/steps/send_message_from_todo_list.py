from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import survey


@given('the respondent is on their todo list')
@when('the respondent navigates to their surveys todo list')
def surveys_todo_list():
    survey.go_to()


@then('the respondent is able to send a message')
def able_to_send_message_for_survey_ru():
    browser.find_by_id('create-message-link-1')


@given('the respondent chooses to send message to ONS')
@given('the respondent is sending a message in relation to bricks')
@when('the respondent chooses to send a message for a specific RU and survey')
def select_create_message():
    surveys_todo_list()
    browser.find_by_id('create-message-link-1').click()


@then('the respondent is navigated to the create message page')
def assert_create_message_page():
    browser.find_by_id('secure-message-subject')


@given('the respondent chooses to send a valid message to ONS')
@when('the respondent enters a valid message')
def enter_valid_message():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('123')
    browser.driver.find_element_by_id('secure-message-body').send_keys('345')


@then('the message will be sent to the internal Bricks mailbox')
def message_sent_to_bricks_workgroup():
    current_url = browser.driver.current_url
    assert 'survey=cb8accda-6118-4d3b-85a3-149e28960c54' in current_url


@when('the respondent enters more than 96 characters in the subject field')
def subject_field_too_long():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('x' * 98)
    browser.driver.find_element_by_id('secure-message-body').send_keys('y' * 200)


@when('chooses to send the message')
@when('the message is sent')
@when('selects to send message')
def click_send_message_btn():
    browser.find_by_id('send-message-btn').click()


@then('an error message appears specifying subject too long')
def check_for_error_subject_too_long():
    browser.driver.find_element_by_link_text('Subject field length must not be greater than 100')


@when('the respondent enters more than 10000 characters in the body field')
def body_too_long():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('x' * 50)
    browser.driver.find_element_by_id('secure-message-body').send_keys('y' * 11000)


@then('an error message appears specifying body too long')
def check_for_body_too_long_error():
    browser.driver.find_element_by_link_text('Body field length must not be greater than 10000')


@when('the respondent tries to send the message without populating the body and subject fields')
def empty_subject_and_body_fields():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('')
    browser.driver.find_element_by_id('secure-message-body').send_keys('')


@then('an error message appears specifying body and subject fields are required')
def error_require_body_and_subject():
    browser.driver.find_element_by_link_text('Please enter a subject')
    browser.driver.find_element_by_link_text('Please enter a message')


@then('the respondent is navigated to their inbox')
def navigated_to_inbox():
    browser.driver.find_element_by_id('inbox-list').find_element_by_class_name('navigation-tabs__tab navigation-tabs__tab--active')


@then('the respondent is navigated to their inbox and notified message sent successfully')
def navigated_to_inbox_show_message_sent_notif():
    browser.driver.find_element_by_id('inbox-list').find_element_by_class_name('navigation-tabs__tab navigation-tabs__tab--active')


@when('the respondent populates the body field but not the subject and chooses to send message')
def populate_body_not_subject():
    browser.driver.find_element_by_id('secure-message-body').send_keys('123')


@then('an error message appears specifying subject must be populated')
def assert_error_no_subject():
    browser.driver.find_element_by_link_text('Please enter a message')


@when('the respondent populates the subject field but not the body field')
def populate_subject_no_body():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('456')


@then('an error message appears notifying the respondent a body must be supplied')
def assert_error_no_subject():
    browser.driver.find_element_by_link_text('Please enter a subject')
