from behave import given, when, then

from acceptance_tests.features.pages import sign_in_respondent, change_enrolment_status, reporting_unit, surveys_todo


@given('the internal user is on the ru details page')
@when('the internal user is back on the ru details page')
def internal_user_view_ru_details(_):
    reporting_unit.go_to('49900000001')

@given('the internal user disables enrolment for respondent with email "{email}"')
def internal_user_disables_enrolment(_, email):
    reporting_unit.go_to('49900000001')
    reporting_unit.click_data_panel('Bricks')
    reporting_unit.click_change_enrolment(email)
    change_enrolment_status.confirm_change_enrolment_status()
    reporting_unit.click_data_panel('Bricks')
    respondent = reporting_unit.get_respondent('Bricks', email)
    assert respondent['enrolmentStatus'] == 'Disabled'


@when('the internal clicks on the disable button for "{email}"')
@when('the internal clicks on the re-enable button for "{email}"')
def click_change_respondent_enrolment(_, email):
    reporting_unit.click_data_panel('Bricks')
    reporting_unit.click_change_enrolment(email)


@when('the internal user confirms they want to disable the account')
@when('the internal user confirms they want to re-enable the account')
def confirm_disable_respondent_enrolment(_):
    change_enrolment_status.confirm_change_enrolment_status()


@when('the respondent with email "{email}" views their survey todo list')
def view_surveys_todo(_, email):
    sign_in_respondent.signed_in_respondent_with_email(email)
    surveys_todo.go_to()


@then('"{email}"\'s enrolment appears "{status}" on the ru details page')
def enrolment_is_disabled(_, email, status):
    reporting_unit.click_data_panel('Bricks')
    respondent = reporting_unit.get_respondent('Bricks', email)
    
    assert respondent['enrolmentStatus'] == status


@then('the respondent should not be able to view the disabled enrolment')
def respondent_enrolment_is_disabled(_):
    surveys_list = surveys_todo.get_surveys_list()
    assert 'You have no surveys to complete' in surveys_list.value


@then('the respondent should see the survey in their todo list')
def respondent_enrolment_is_not_disabled(_):
    surveys_list = surveys_todo.get_surveys_list()
    assert 'You have no surveys to complete' not in surveys_list.value
