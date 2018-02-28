from behave import when

from acceptance_tests.features.pages import change_response_status


@when('the internal user changes the response status from \'Not started\' to \'Completed by phone\'')
def internal_user_changes_response_status(_):
    change_response_status.update_response_status('COMPLETED_BY_PHONE')

