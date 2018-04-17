from behave import given, when, then

from acceptance_tests.features.pages import change_enrolment_status, reporting_unit


@given('the internal user is on the ru details page')
def internal_user_view_ru_details(_):
    reporting_unit.go_to('49900000001')


@when('the internal clicks on the disable button')
def click_disable_respondent_enrolment(_):
    reporting_unit.click_disable_enrolment()


@when('the internal user confirms they want to disable the account')
def confirm_disable_respondent_enrolment(_):
    change_enrolment_status.confirm_change_enrolment_status()


@then("the respondent's enrolment appears disabled on the ru details page")
def enrolment_is_disabled(_):
    respondents = reporting_unit.get_associated_respondents()
    pass