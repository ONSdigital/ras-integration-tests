from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import add_survey
from acceptance_tests.features.pages import surveys_todo
from acceptance_tests.features.pages.reporting_unit import get_unused_iac
from acceptance_tests.features.steps.authentication import signed_in_internal


@given('the respondent has a CE for an eQ available')
def respondent_has_eq_ce_available(context):
    # go_live event datetime is currently being hacked to an earlier date in qbs_1809_setup.sql script
    signed_in_internal(context)
    enrolment_code = get_unused_iac(49900000005, 'QBS')
    add_survey.go_to()
    browser.driver.find_element_by_id('ENROLEMENT_CODE_FIELD').send_keys(enrolment_code)
    browser.find_by_id('CONTINUE_BTN').click()
    browser.find_by_id('CONFIRM_SURVEY_BTN').click()


@when('the respondent accesses the eQ CE')
def respondent_accesses_eq_ce(_):
    surveys_todo.go_to()
    surveys_todo.access_survey('Quarterly Business Survey')


@then('the respondent lands on the correct eQ Homepage for the survey and CE and CI')
def respondent_redirected_to_eq(_):
    url = browser.url
    assert 'https://eq-test/session?token=' in url
    token = url[30:]
    assert len(token.split('.')) == 5   # check correct jwt format
