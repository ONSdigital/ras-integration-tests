from behave import given, when, then
from acceptance_tests import browser

from acceptance_tests.features.pages import edit_respondent_details_form, reporting_unit


@given('the internal user has found the respondents details for 49900000001')
def internal_user_find_respondent_details(_):
    reporting_unit.go_to('49900000001')
    reporting_unit.click_data_panel('Bricks')


@when('they choose to change the name of a respondent')
def click_edit_details(_):
    reporting_unit.click_edit_details()


@given('the internal user chooses to change the account details')
def open_edit_details(_):
    reporting_unit.go_to('49900000001')
    reporting_unit.click_data_panel('Bricks')
    reporting_unit.click_edit_details()


@when('they change the first and last name')
def edit_first_last_name(_):
    edit_respondent_details_form.edit_first_name('Jacky')
    edit_respondent_details_form.edit_last_name('Turner')


@when('they remove the old contact number')
def clear_old_contact_number(_):
    edit_respondent_details_form.clear_telephone_number()


@when('they change the contact number')
def change_contact_number(_):
    edit_respondent_details_form.edit_contact_number("01633 878787")


@then('the respondent account details become editable')
@then('the changes will not be saved and they are informed that all fields are required')
def fields_required(_):
    # TODO: Modify test once Technical backlog card has been complete for error messages
    assert browser.title == 'Edit contact details'


@when('they click save')
@when('they click save and the details are unable to be saved')
def click_save(_):
    edit_respondent_details_form.click_save()


@when('they decide to cancel')
def cancel_changes(_):
    edit_respondent_details_form.click_cancel()


@then('they are navigated back to the RU Details page')
@then('they are able to enter up to 254 characters')
def navigate_to_ru_details(_):
    assert " | Reporting units | Survey Data Collection" in browser.title


@then('they are provided with confirmation the changes have been saved')
def confirm_changes_saved(_):
    assert reporting_unit.confirm_contact_details_changes()


@then('the contact number is not changed')
def confirm_contact_number_unchanged(_):
    reporting_unit.click_data_panel('Bricks')
    respondent = reporting_unit.get_associated_respondents()[0]
    assert respondent.get('phone') == '01633 878787'
