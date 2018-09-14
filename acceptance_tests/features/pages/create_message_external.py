from acceptance_tests import browser


def enter_valid_subject(subject):
    browser.driver.find_element_by_id('secure-message-subject').send_keys(subject)


def enter_valid_body(body):
    browser.driver.find_element_by_id('secure-message-body').send_keys(body)


def get_subject_and_body():
    form_text_fields = browser.find_by_id("secure-message-form").first
    form_text_field_attributes = {'subject': form_text_fields.find_by_id('secure-message-subject').value,
                                  'body': form_text_fields.find_by_id('secure-message-body').value}
    return form_text_field_attributes


def get_message_body_text():
    return get_subject_and_body().get('body')


def enter_valid_body_over_80_character_summary():
    browser.driver.find_element_by_id('secure-message-body').send_keys('I would like to query data. ' * 5)


def enter_invalid_length_subject():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('x' * 98)


def send_message():
    browser.find_by_id('send-message-btn').click()


def enter_invalid_length_body():
    browser.execute_script(f'document.getElementById("secure-message-body").value="{"x" * 9990}";')
    browser.driver.find_element_by_id('secure-message-body').send_keys('y' * 100)


def empty_subject():
    browser.driver.find_element_by_id('secure-message-subject').clear()


def empty_body():
    browser.driver.find_element_by_id('secure-message-body').clear()
