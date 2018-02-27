from logging import getLogger
import time

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests.features.pages import collection_exercise_details
from controllers import (collection_exercise_controller, sample_controller,
                         collection_instrument_controller)

logger = wrap_logger(getLogger(__name__))


@given('the collection exercises are in the ready for review state')
def prepare_collection_exercises(_):
    rsi_id = '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c'
    sample_file = 'resources/sample_files/business-survey-sample-date.csv'
    ci_path = 'resources/collection_instrument_files/064_0001_201803.xlsx'

    for period in ('201812', '201811'):
        state = collection_exercise_controller.get_collection_exercise(rsi_id, period)['state']
        if state == 'SCHEDULED':
            logger.info('Loading sample', survey='rsi', period=period)
            sample_controller.load_sample('rsi', period, sample_file)

            logger.info('Loading collection instrument', survey='rsi', period=period)
            ce = collection_exercise_controller.get_collection_exercise(rsi_id, period)
            collection_instrument_controller.upload_collection_instrument(ce['id'], ci_path)

            for i in range(5):
                state = collection_exercise_controller.get_collection_exercise(rsi_id, period)['state']
                if state == 'READY_FOR_REVIEW':
                    break
                time.sleep(1)

        assert state == 'READY_FOR_REVIEW', state


@given('the user has checked the contents of the collection exercise and it is all correct')
def user_checks_ce_contents(context):
    collection_exercise_details.go_to(context.survey, context.survey_period)
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Ready for Review', ce_state
    assert collection_exercise_details.ready_for_live_button_exists(), collection_exercise_details.ready_for_live_button_exists()
    cis = collection_exercise_details.get_collection_instruments()
    assert 'test_collection_instrument.xlxs' in cis
    sample = collection_exercise_details.get_loaded_sample()
    assert 'Total businesses' in sample
    assert 'Collection instruments' in sample
    assert '1' in sample


@when('they confirm set the collection exercise as ready to go live')
def set_ready_for_live(_):
    collection_exercise_details.click_ready_for_live_and_confirm()
    success_text = collection_exercise_details.get_execution_success()
    assert success_text == 'Collection exercise executed'


@when('they choose to set the collection exercise as ready for live')
def click_set_ready(_):
    collection_exercise_details.click_ready_for_live()


@then('the collection exercise state is changed to Setting Ready for Live')
def view_ready_for_live(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Setting Ready for Live'


@then('they are asked for confirmation before continuing')
def check_confirmation(_):
    alert = collection_exercise_details.get_confirmation_alert()
    assert alert.text == 'There\'s no going back...'
    alert.dismiss()
