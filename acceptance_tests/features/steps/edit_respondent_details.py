from behave import given, when, then
from acceptance_tests import browser

from acceptance_tests.features.pages import edit_respondent_details_form, reporting_unit


@given('the internal user has found the respondents details for 49900000001')
@given('the internal user chooses to change the account details')
def internal_user_find_respondent_details(_):
    edit_respondent_details_form.go_to('49900000001')
    reporting_unit.click_data_panel('Bricks')


@when('they choose to change the name of a respondent')
def change_respondent_name(_):
    edit_respondent_details_form.click_edit_details()


@then('the respondent account details become editable')
def account_details_editable(_):
    edit_respondent_details_form.edit_first_name()


@when('they change the first and last name')
def edit_first_last_name(_):
    edit_respondent_details_form.click_edit_details()


@then('they are able to enter up to 254 characters')
def able_to_enter_254_characters(_):
    edit_respondent_details_form.edit_first_name()
    edit_respondent_details_form.edit_last_name()


@given('the internal user chooses to change the contact number of a respondent')
def change_respondent_number(_):
    edit_respondent_details_form.go_to()
    edit_respondent_details_form.click_edit_details()


@when('they remove the old contact number and click save')
def clear_old_contact_number(_):
    browser.driver.find_element_by_id('telephone').clear()


@then('the changes will not be saved and they are informed that all fields are required')
def fields_required(_):
    # TODO: Modify test once Technical backlog card has been complete for error messages
    browser.driver.find_element_by_id()


@when('they change the contact number and save the changes')
def change_contact_number_and_save(_):
    edit_respondent_details_form.edit_contact_number()


@then('they are navigated back to the RU Details page')
def navigate_to_ru_details(_):
    assert browser.title == " | Reporting units | Survey Data Collection"


@when('they click save and the details are unable to be saved')
def click_save(_):
    edit_respondent_details_form.click_save()


@then('they are informed that an error occurred and to try again')
def save_changes_error(_):
    browser.driver.find_element_by_id('error-saving-message')


@then('provided with confirmation the changes have been saved')
def confirm_changes(_):
    browser.driver.find_element_by_id('contact-changed')


@when('they decide to cancel')
def cancel_changes(_):
    browser.driver.find_element_by_id('cancel-btn').click()


@then('they are navigated back to the RU Details page and no changes are saved')
def no_changes_saved(_):
    assert browser.title == " | Reporting units | Survey Data Collection"
