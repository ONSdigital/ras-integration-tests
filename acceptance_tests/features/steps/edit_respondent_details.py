from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.environment import register_respondent
from acceptance_tests.features.pages import edit_respondent_details_form, reporting_unit
from config import Config
from controllers.party_controller import get_party_by_ru_ref, get_respondent_details, get_party_by_email


@given('the respondent with email "test_respondent@test.com" is enrolled')
def respondent_email_is_enrolled(_):
    business = get_party_by_ru_ref('49900000001')
    respondent_id = business['associations'][0]['partyId']
    respondent = get_respondent_details(respondent_id)
    if respondent['emailAddress'] != 'test_respondent@test.com':
        reporting_unit.go_to('49900000001')
        reporting_unit.click_data_panel('Bricks')
        reporting_unit.click_edit_details('Bricks')
        edit_respondent_details_form.edit_email_address('test_respondent@test.com')
        edit_respondent_details_form.click_save()


@given('the internal user has found the respondents details')
@given('the internal user chooses to change the account details')
@given('the user chooses to change a respondents email address')
def open_edit_details(_):
    reporting_unit.go_to('49900000001')
    reporting_unit.click_data_panel('Bricks')
    reporting_unit.click_edit_details('Bricks')


@when('they choose to change the name of a respondent')
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


@when('they change the email address')
def edit_email_address(_):
    edit_respondent_details_form.edit_email_address(Config.RESPONDENT_USERNAME)


@when('they save an email address that is already in use')
def save_email_already_in_use(_):
    existing_email = 'existing_respondent@email.com'
    email_found = get_party_by_email(existing_email)
    if not email_found:
        register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                            username=existing_email)
    edit_respondent_details_form.edit_email_address(existing_email)
    edit_respondent_details_form.click_save()


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
@then('they are able to save the updated email address')
def confirm_changes_saved(_):
    assert reporting_unit.get_confirm_contact_details_success_text()


@then('they are provided with confirmation that the email address has been changed')
@then('they are presented with confirmation that the changes have been saved')
def confirm_email_changes_saved(_):
    contact_details_changes = reporting_unit.get_confirm_contact_details_success_text()
    assert 'Verification email sent to' in contact_details_changes


@then('the contact number is not changed')
def confirm_contact_number_unchanged(_):
    reporting_unit.click_data_panel('Bricks')
    respondent = reporting_unit.get_associated_respondents()[0]
    assert respondent.get('phone') == '01633 878787'


@then('the email is not changed')
def confirm_email_unchanged(_):
    reporting_unit.click_data_panel('Bricks')
    respondent = reporting_unit.get_associated_respondents()[0]
    assert respondent.get('email') == Config.RESPONDENT_USERNAME


@then('they are informed that the email address they have entered is already in use')
def error_email_already_in_use(_):
    assert reporting_unit.save_email_error()
