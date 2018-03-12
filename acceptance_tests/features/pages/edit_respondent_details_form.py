from acceptance_tests import browser
from config import Config


def go_to(ru_ref):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/reporting-units/{ru_ref}")


def edit_first_name():
    browser.find_by_id('firstName').fill('Jacky')


def first_name_254_characters():
    browser.execute_script(f'document.getElementById("firstName").value="{"x" * 254}";')


def last_name_254_characters():
    browser.execute_script(f'document.getElementById("firstName").value="{"x" * 254}";')


def edit_contact_number():
    browser.driver.find_element_by_id('telephone').send_keys('01633 878787')


def click_save():
    browser.driver.find_element_by_id('save-btn').click()


def click_edit_details():
    browser.find_by_id('edit-contact-details-btn').click()
