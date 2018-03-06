from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests.features.pages import enrolment_code, reporting_unit

logger = wrap_logger(getLogger(__name__))


@given('the internal user views the 49900000001 reporting unit page')
def internal_user_views_the_reporting_unit(_):
    reporting_unit.go_to('49900000001')


@when('the user clicks generate enrolment code')
def internal_user_generates_new_code(_):
    reporting_unit.click_generate_new_code()


@then('a new enrolment code is displayed back to the user')
def internal_user_views_generated_code(_):
    iac = enrolment_code.get_iac()
    assert iac
