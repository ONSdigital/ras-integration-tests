from behave import given, when, then
from acceptance_tests import browser

from acceptance_tests.features.pages import edit_respondent_details_form


@given('the internal user has found the respondents details')
def internal_user_find_respondent_details(_):
    pass


@when('they choose to change the name of a respondent')
def change_respondent_name(_):
    pass


@then('the respondent account details become editable')
def account_details_editable(_):
    pass


@given('the internal user chooses to change account details')
def change_respondent_name(_):
    edit_respondent_details_form.go_to()


@when('they change the first and last name')
def edit_first_last_name(_):
    browser.driver.find_element_by_id('edit-contact-details-btn').click()


@then('they are able to enter up to 254 characters')
def able_to_enter_254_characters(_):
    edit_respondent_details_form.edit_first_name()
    edit_respondent_details_form.edit_last_name()

# TODO: Add in Scenario 3 steps when scenario has been clarified


@when('they change the contact number and and save')
def change_contact_number_and_save(_):
    edit_respondent_details_form.edit_contact_number()


@then('they are navigated back to the RU Details page')
def navigate_to_ru_details(_):
    pass


@then('provided with confirmation the changes have been saved')
def confirm_changes(_):
    pass


@when('they decide to cancel')
def cancel_changes(_):
    browser.driver.find_element_by_id('cancel-btn').click()


@then('they are navigated back to the RU Details page and no changes are saved')
def no_changes_saved(_):
    pass
