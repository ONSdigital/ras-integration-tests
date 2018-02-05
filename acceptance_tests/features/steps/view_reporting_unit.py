from behave import given, when, then

from acceptance_tests.features.pages import common, reporting_unit


@given('The internal user has accessed the page reporting unit page')
def internal_user_views_the_survey_page(_):
    reporting_unit.go_to('49900000001')


@when('The internal has accessed the page reporting unit page')
def internal_user_views_the_survey_page(_):
    assert common.get_page_title() == 'RUNAME1_COMPANY1 RUNNAME2_COMPANY1 | Reporting units | Survey Data Collection'


@then('The user should see the RU Ref')
def internal_user_views_the_survey_page(_):
    assert reporting_unit.get_ru_ref() == '49900000001'
