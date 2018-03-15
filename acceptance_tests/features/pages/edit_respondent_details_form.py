from acceptance_tests import browser


def edit_first_name():
    browser.find_by_id('firstName').fill('Jacky')


def edit_last_name():
    browser.find_by_id('firstName').fill('Turner')


def clear_telephone_number():
    browser.find_by_id('telephone').fill("")


def edit_contact_number():
    browser.find_by_id('telephone').fill("01633 878787")


def click_save():
    browser.find_by_id('save-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()
