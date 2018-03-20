from acceptance_tests import browser


def edit_first_name(name):
    browser.find_by_id('firstName').fill(name)


def edit_last_name(name):
    browser.find_by_id('lastName').fill(name)


def clear_telephone_number():
    browser.find_by_id('telephone').fill("")


def edit_contact_number(number):
    browser.find_by_id('telephone').fill(number)


def click_save():
    browser.find_by_id('save-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()


def edit_email_address(email):
    browser.find_by_id('email').fill(email)
