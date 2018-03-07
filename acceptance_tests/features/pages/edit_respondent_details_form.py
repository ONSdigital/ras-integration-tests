from acceptance_tests import browser


def go_to(ru_ref):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/reporting-units/{ru_ref}")


def edit_first_name():
    browser.driver.find_element_by_id('firstName').send_keys('Jacky')


def edit_last_name():
    browser.driver.find_element_by_id('lastName').send_keys('Turner')


def first_name_254_characters():
    browser.execute_script(f'document.getElementById("firstName").value="{"x" * 254}";')


def last_name_254_characters():
    browser.execute_script(f'document.getElementById("firstName").value="{"x" * 254}";')


def edit_contact_number():
    browser.driver.find_element_by_id('telephone').send_keys('01633 878787')


def click_save():
    browser.driver.find_element_by_id('save-btn').click()
