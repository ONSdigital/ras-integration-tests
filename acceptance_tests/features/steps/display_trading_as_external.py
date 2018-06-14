from contextlib import suppress

from behave import given, then, when

from acceptance_tests import browser
from acceptance_tests.features.environment import wait_for_ru_specific_cases_to_update
from acceptance_tests.features.pages.surveys_history import go_to_history_tab
from acceptance_tests.features.pages.surveys_todo import go_to as go_to_todo
from acceptance_tests.features.steps.authentication import signed_in_respondent
from controllers.case_controller import generate_new_enrolment_code, update_case_group_status
from controllers.collection_exercise_controller import get_collection_exercise
from controllers.party_controller import add_survey, get_party_by_email


@given('a company with "{ru_ref}" has a separate trading name')
def company_has_separate_trading_name_s01(_, ru_ref):
    ce_id = get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201801')['id']
    _add_survey_for_ru_to_respondent_suppress_exception('example@example.com', ru_ref, ce_id)


@when('the respondent views a survey in To do')
def respondent_views_survey_in_todo(_):
    go_to_todo()


@then('the "trading as" name should be displayed below the business name for every survey')
def trading_as_name_is_displayed_below_business_name_in_todo(_):
    assert 'BOLTS LTD' in browser.driver.find_element_by_id('REPORTING_UNIT_DETAILS_49900000006').text,\
        'could not find trading as name "BOLTS LTD" in respondent todo page'


@when('the respondent has completed a survey which is now in their history')
def respondent_has_completed_survey(_):

    # Complete the survey by phone
    ru_ref = '49900000007'
    party_id = get_party_by_email('example@example.com')['id']
    wait_for_ru_specific_cases_to_update(party_id, ru_ref)
    ce_id = get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201801')['id']
    update_case_group_status(ce_id, ru_ref, 'COMPLETED_BY_PHONE')

    # Ensure respondent is signed in and navigate to history
    signed_in_respondent(_)
    go_to_history_tab()


@then('the trading name should be displayed below the business name for every survey')
def trading_as_name_is_displayed_below_business_name_in_history(_):
    assert 'PC LTD' in browser.driver.find_element_by_id('REPORTING_UNIT_DETAILS_49900000007').text,\
        'Could not find trading as name "PC LTD" in respondent history page'


@given('a company does not have a separate "trading as" name')
def company_does_not_have_trading_as_name(_):
    ce_id = get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201801')['id']
    _add_survey_for_ru_to_respondent_suppress_exception('example@example.com', '49900000008', ce_id)


@then('the "trading as" field should not appear on the RU details page')
def trading_as_field_does_not_appear(_):
    assert 'Trading as:' not in browser.driver.find_element_by_id('REPORTING_UNIT_DETAILS_49900000008').text,\
        'Found "trading as" for a business that does not have a trading as name in respondent todo page'


def _get_last_QBS_collection_exercise_id():
    return get_collection_exercise('02b9c366-7397-42f7-942a-76dc5876d86d', '1809')['id']


def _add_survey_for_ru_to_respondent_suppress_exception(respondent_email, ru_ref, collection_exercise_id):
    enrolment_code = generate_new_enrolment_code(collection_exercise_id, ru_ref)['iac']

    # Suppress exception in case the survey has already been added
    with suppress(Exception):
        add_survey(get_party_by_email(respondent_email)['id'], enrolment_code)
