from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import edit_respondent_details_form, reporting_unit
from common.respondent_utilities import register_respondent
from common.survey_utilities import make_email_address
from controllers.database_controller import get_different_respondent_email_address
from controllers.party_controller import get_party_by_email


@given('the respondent with email "{email}" is enrolled and active')
def respondent_is_enrolled_and_active(_, email):
    create_respondent(email)


@given('the internal user chooses to change account details')
@given('the internal user has found the respondents details')
def open_edit_details_change_email(context):
    reporting_unit.go_to(context.short_name)
    reporting_unit.click_data_panel(context.short_name)
    reporting_unit.click_edit_details(context.short_name, context.user_name)


@when('they choose to change the name of a respondent')
@when('they change the first and last name')
def edit_first_last_name(context):
    edit_respondent_details_form.edit_first_name('Jacky')
    edit_respondent_details_form.edit_last_name('Turner')


@when('they remove the old contact number')
def clear_old_contact_number(_):
    edit_respondent_details_form.clear_telephone_number()


@when('they change the contact number')
def change_contact_number(context):
    edit_respondent_details_form.edit_contact_number(context.phone_number)


@when('they change the email address')
def edit_email_address(context):
    context.changed_email_address = make_email_address()
    edit_respondent_details_form.edit_email_address(context.changed_email_address)


@when('they save an email address that is already in use')
def save_email_already_in_use(context):
    context.used_email_address = get_different_respondent_email_address(context.user_name)
    edit_respondent_details_form.edit_email_address(context.used_email_address)
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
    assert 'Contact details changed and verification email sent to' in contact_details_changes, contact_details_changes


@then('they can see the old and the unverified new email')
def view_pending_email(context):
    reporting_unit.click_data_panel(context.short_name)
    respondent = reporting_unit.get_respondent(context.short_name, context.user_name)
    assert respondent.get('email') == context.user_name
    assert respondent.get('pending_email') == context.changed_email_address


@then('the contact number is not changed')
def confirm_contact_number_unchanged(context):
    reporting_unit.click_data_panel(context.short_name)
    respondent = reporting_unit.get_associated_respondents(context.short_name)[0]
    assert respondent.get('phone') == context.phone_number


@then('the email is not changed')
def confirm_email_unchanged(context):
    reporting_unit.click_data_panel(context.short_name)
    respondent = reporting_unit.get_associated_respondents(context.short_name)[0]
    assert respondent.get('email') == context.user_name


@then('they are informed that the email address they have entered is already in use')
def error_email_already_in_use(_):
    assert reporting_unit.save_email_error()


def create_respondent(email):
    email_in_use = get_party_by_email(email)
    if not email_in_use:
        register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                            username=email, ru_ref=49900000001)
