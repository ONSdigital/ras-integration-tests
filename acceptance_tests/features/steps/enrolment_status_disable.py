from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit


@given('the internal user is on the ru details page')
def internal_user_view_ru_details():
    reporting_unit.go_to('49900000001')

@when('the internal user requests a respondent enrolment to be disabled')
def choose_to_disable_respondent_enrolment():
