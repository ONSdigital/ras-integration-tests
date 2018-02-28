from logging import getLogger
import time

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests.features.pages import collection_exercise_details
from controllers import (collection_exercise_controller, sample_controller,
                         collection_instrument_controller)

logger = wrap_logger(getLogger(__name__))


@given('the collection exercise is in the ready for review state')
def prepare_collection_exercises(context):
    survey = context.survey
    s_id = context.survey_id
    period = context.survey_period
    sample_file = 'resources/sample_files/business-survey-sample-date.csv'
    ci_path = 'resources/collection_instrument_files/064_0001_201803.xlsx'

    state = collection_exercise_controller.get_collection_exercise(s_id, period)['state']

    if state == 'SCHEDULED':
        logger.info('Loading sample', survey=survey, period=period)
        sample_controller.load_sample(survey, period, sample_file)

        logger.info('Loading collection instrument', survey=survey, period=period)
        ce = collection_exercise_controller.get_collection_exercise(s_id, period)
        collection_instrument_controller.upload_collection_instrument(ce['id'], ci_path)

    for i in range(5):
        state = collection_exercise_controller.get_collection_exercise(s_id, period)['state']
        if state == 'READY_FOR_REVIEW':
            break
        time.sleep(1)


@given('the user has confirmed that the collection exercise is ready for go live')
def confirmed_ready(context):
    collection_exercise_details.go_to(context.survey, context.survey_period)
    collection_exercise_details.click_ready_for_live_and_confirm()
    success_text = collection_exercise_details.get_execution_success()
    assert success_text == 'Collection exercise executed'


@given('the user has checked the contents of the collection exercise and it is all correct')
def user_checks_ce_contents(context):
    collection_exercise_details.go_to(context.survey, context.survey_period)
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Ready for Review', ce_state
    assert collection_exercise_details.ready_for_live_button_exists()
    assert len(collection_exercise_details.get_collection_instruments()) > 0
    sample = collection_exercise_details.get_loaded_sample()
    assert 'Total businesses' in sample
    assert 'Collection instruments' in sample
    assert '1' in sample


@when('they navigate to the collection exercise details screen')
def navigate_to_ce(context):
    collection_exercise_details.go_to(context.survey, context.survey_period)


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
    assert ce_state == 'Setting Ready for Live'
    info_panel = collection_exercise_details.get_processing_info()
    assert 'Processing' in info_panel


@then('when refreshing the page once processing has completed, the status is changed to Ready for Live')
def refresh_ready_for_live(_):
    collection_exercise_details.click_refresh_link()
    for i in range(5):
        ce_state = collection_exercise_details.get_status()
        if ce_state == 'Ready for Live':
            break
        time.sleep(1)
        collection_exercise_details.click_refresh_link()
    assert ce_state == 'Ready for Live'


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
