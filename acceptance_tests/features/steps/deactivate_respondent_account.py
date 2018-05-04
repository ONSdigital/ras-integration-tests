from behave import given, when, then

from controllers.party_controller import get_party_by_email
from acceptance_tests.features.pages import change_account_status, reporting_unit, sign_in_respondent


@given('the internal user is on the reporting unit details page')
def internal_user_on_ru_details_page(_):
    reporting_unit.go_to("49900000001")


@given("the internal user has selected to deactivate a respondent {email} account")
@when("the internal user selects to deactivate respondent's {email} account")
def select_deactivate_account(_, email):
    reporting_unit.click_data_panel('Bricks')
    reporting_unit.click_deactivate_account(email)


@then("all the respondent's enabled enrolments should be displayed")
def view_respondent_enabled_enrolments(_):
    enrolment = change_account_status.find_enrolment("49900000001", "Bricks")

    assert enrolment is not "Enrolment not found"


@when("the internal user confirms suspension of account")
def confirm_suspend_account(_):
    change_account_status.confirm_change_account_status()


@then("the respondent {email} account is suspended")
def account_suspended(_, email):
    reporting_unit.go_to("49900000001")
    reporting_unit.click_data_panel('Bricks')
    account_status = reporting_unit.get_respondent_account_status(email)

    assert account_status is "Suspended"


@then("confirmation of suspended account presented to user")
def notification_of_suspension_of_account(_):
    success_notif = reporting_unit.get_confirm_success_text()

    assert "Account status changed" in success_notif


@given("respondent with email {email} has a suspended account")
def check_respondent_has_suspended_account(_, email):
    # TODO: replace this with check for respondent account suspended when all respondents are returned via email

    respondent = get_party_by_email(email)

    assert respondent is None


@when("the suspended respondent attempts to sign in with email {email}")
def suspended_respondent_attempts_sign_in(_, email):
    sign_in_respondent.signed_in_respondent_with_email(email)


@then("presented with notification of wrong login details")
def notification_incorrect_login(_):
    sign_in_respondent.error_incorrect_login_details()
