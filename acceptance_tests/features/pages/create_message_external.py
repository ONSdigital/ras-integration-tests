from acceptance_tests import browser


def enter_valid_subject():
    browser.driver.find_element_by_id('secure-message-subject').send_keys('123')


def enter_valid_body():
    browser.driver.find_element_by_id('secure-message-body').send_keys('345')


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
