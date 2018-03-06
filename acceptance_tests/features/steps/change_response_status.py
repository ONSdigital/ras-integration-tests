from behave import when, given, then

from acceptance_tests import browser
from acceptance_tests.features.pages.reporting_unit import get_unused_iac
from acceptance_tests.features.steps.authentication import signed_in_internal, signed_in_respondent
from acceptance_tests.features.pages import add_survey, change_response_status, surveys_history, reporting_unit


@given('the survey for 49900000002 has been completed by phone')
def survey_for_49900000002_completed_by_phone(_):
    ru_ref = '49900000002'
    _change_response_status(_, ru_ref)
    _enrol_respondent_with_ru_ref(_, ru_ref)


@when('the respondent goes to the history page')
def respondent_goes_to_history_page_for_49900000002(_):
    signed_in_respondent(_)
    surveys_history.go_to_history_tab()


@when('the internal user changes the response status from \'Not started\' to \'Completed by phone\' for {ru_ref}')
def internal_user_changes_response_status(_, ru_ref):
    reporting_unit.click_change_response_status_link(ru_ref=ru_ref, survey='Bricks', period='201801')
    change_response_status.update_response_status('COMPLETED_BY_PHONE')


@then('the survey for 49900000002 has the status completed by phone')
def survey_for_49900000002_shows_status_completed_by_phone(_):
    status = surveys_history.get_status_text()
    assert status == 'Completed by phone'


def _enrol_respondent_with_ru_ref(_, ru_ref):
    signed_in_internal(_)
    enrolment_code = get_unused_iac(ru_ref, 'Bricks')

    signed_in_respondent(_)
    add_survey.go_to()
    browser.driver.find_element_by_id('ENROLEMENT_CODE_FIELD').send_keys(enrolment_code)
    browser.find_by_id('CONTINUE_BTN').click()
    browser.find_by_id('CONFIRM_SURVEY_BTN').click()


def _change_response_status(_, ru_ref):
    signed_in_internal(_)
    reporting_unit.go_to(ru_ref)
    internal_user_changes_response_status(_, ru_ref)
