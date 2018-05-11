from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details  # NOQA
from common.browser_utilities import is_text_present_with_retry
from controllers import (collection_exercise_controller, sample_controller,
                         collection_instrument_controller)

logger = wrap_logger(getLogger(__name__))


def _get_survey_id(survey):
    return {
        'rsi': '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c',
        'bricks': 'cb8accda-6118-4d3b-85a3-149e28960c54',
    }.get(survey.lower())


@given('"{survey}" "{period}" is in the ready for review state')
def prepare_collection_exercises(_, survey, period):
    s_id = _get_survey_id(survey)
    sample_file = 'resources/sample_files/business-survey-sample-date.csv'
    ci_path = 'resources/collection_instrument_files/064_201803_0001.xlsx'

    state = collection_exercise_controller.get_collection_exercise(s_id, period)['state']

    if state == 'SCHEDULED':
        logger.info('Loading sample', survey=survey, period=period)
        sample_controller.load_sample(survey, period, sample_file)

        logger.info('Loading collection instrument', survey=survey, period=period)
        ce = collection_exercise_controller.get_collection_exercise(s_id, period)
        # form type hard coded to 0001 for all ces to simplify testing
        collection_instrument_controller.upload_seft_collection_instrument(ce['id'], ci_path, '0001')

    is_text_present_with_retry('Ready for review', 10)


@given('the user has confirmed that "{survey}" "{period}" is ready for go live')
def confirmed_ready(_, survey, period):
    collection_exercise_details.go_to(survey, period)
    collection_exercise_details.click_ready_for_live_and_confirm()
    success_text = collection_exercise_details.get_execution_success()
    assert success_text == 'Collection exercise executed'


@given('the user has checked the contents of "{survey}" "{period}" and it is all correct')
def user_checks_ce_contents(_, survey, period):
    collection_exercise_details.go_to(survey, period)
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_review(ce_state), ce_state
    assert collection_exercise_details.ready_for_live_button_exists()
    assert len(collection_exercise_details.get_collection_instruments()) > 0
    sample = collection_exercise_details.get_loaded_sample()
    assert 'Total businesses' in sample
    assert 'Collection instruments' in sample
    assert '1' in sample


@when('they navigate to "{survey}" "{period}" details screen')
def navigate_to_ce(_, survey, period):
    collection_exercise_details.go_to(survey, period)


@when('they confirm that the collection exercise is ready to go live')
def set_ready_for_live(_):
    collection_exercise_details.click_ready_for_live_and_confirm()
    success_text = collection_exercise_details.get_execution_success()
    assert success_text == 'Collection exercise executed'


@when('they choose to set the collection exercise as ready for live')
def click_set_ready(_):
    collection_exercise_details.click_ready_for_live()


@when('the system is setting the collection exercise as ready for live')
@then('the user is informed that the collection exercise is setting as ready for live')
@then('they are to be informed that the system is setting the status as Ready for Live')
def view_ready_for_live(_):
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_setting_ready_for_live(ce_state), ce_state
    info_panel = collection_exercise_details.get_processing_info()
    assert 'Processing' in info_panel


@then('when refreshing the page once processing has completed, the status is changed to Ready for Live')
def refresh_ready_for_live(_):
    collection_exercise_details.click_refresh_link_until_ready_for_live()
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state), ce_state


@then('they are asked for confirmation before continuing')
def check_confirmation(_):
    alert = collection_exercise_details.get_confirmation_alert()
    assert alert.text == 'There\'s no going back...'
    alert.dismiss()


@then('the user is able to refresh the page to see if there are any updates to the status')
def able_to_refresh(_):
    collection_exercise_details.click_refresh_link()
    assert collection_exercise_details.get_status() != ''


@then('they are no longer able to change the CIs, Sample or Mandatory Event Dates')
def locked_ci_sample_events(_):
    # NB: events are not currently editable
    assert not(collection_exercise_details.ready_for_live_button_exists())
    assert not(collection_exercise_details.form_select_ci_exists())
    assert not(collection_exercise_details.form_load_ci_exists())
    assert not(collection_exercise_details.form_load_sample_exists())
