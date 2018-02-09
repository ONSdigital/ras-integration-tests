from behave import given, when, then

from acceptance_tests.features.pages import reporting_unit


@given('the reporting unit 49900000001 is in the system')
def reporting_unit_49900000001_is_in_the_system(_):
    pass


@when('the internal user views the 49900000001 reporting unit page')
def internal_user_views_the_survey_page(_):
    reporting_unit.go_to('49900000001')


@then('the internal user is displayed the correct reporting unit details')
def internal_user_views_correct_reporting_unit_details(_):
    ru_details = reporting_unit.get_ru_details()
    assert ru_details['ru_ref'] == '49900000001'
    assert ru_details['name'] == 'RUNAME1_COMPANY1 RUNNAME2_COMPANY1'
