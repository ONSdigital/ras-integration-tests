from behave import when, given, then

from acceptance_tests.features.pages import change_response_status, reporting_unit, \
    surveys_todo


@given('the internal user is on the reporting unit page for 49900000004')
def go_to_reporting_unit(_):
    reporting_unit.go_to('49900000004')
    reporting_unit.click_change_response_status_link(ru_ref='49900000004', survey='Bricks', period='201801')


@when('the internal user changes the response status from \'Completed by phone\' to \'Reopened\'')
def completed_by_phone_to_reopened_status(_):
    change_response_status.update_response_status('COMPLETED_BY_PHONE')
    surveys_todo.get_status_text('Completed by phone')

    reporting_unit.click_change_response_status_link(ru_ref='49900000004', survey='Bricks', period='201801')
    change_response_status.update_response_status('REOPENED')


@then('the status \'Reopened\' is displayed back to the internal user')
def internal_user_status_is_reopened(_):
    status = surveys_todo.get_status_text('Reopened')
    assert status == 'Reopened'


@given('the survey for 49900000004 has been completed by phone')
def completed_by_phone(_):
    reporting_unit.go_to('49900000005')
    reporting_unit.click_change_response_status_link(ru_ref='49900000005', survey='Bricks', period='201801')
    change_response_status.update_response_status('COMPLETED_BY_PHONE')
    surveys_todo.get_status_text('Completed by phone')


@when('the respondent goes to the my surveys page')
def go_to_my_surveys(_):
    reporting_unit.click_change_response_status_link(ru_ref='49900000005', survey='Bricks', period='201801')
    change_response_status.update_response_status('REOPENED')


@then('the survey for 49900000005 has the status reopened')
def respondent_status_is_reopened(_):
    associated_ces = reporting_unit.get_associated_collection_exercises()
    assert 'Reopened' in associated_ces[0]['status']
