
from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from common.browser_utilities import is_text_present_with_retry


@given('the 201809 collection exercise for the RSI survey is Scheduled')
def rsi_201809_exists_and_scheduled_displayed(_):
    collection_exercise_details.go_to('RSI', '201809')
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_scheduled(ce_state), ce_state


@given('the 201810 collection exercise for the RSI survey is Scheduled')
def rsi_201810_exists_and_scheduled_displayed(_):
    collection_exercise_details.go_to('RSI', '201810')
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_scheduled(ce_state), ce_state


@given('the 201811 collection exercise has a loaded sample and collection instruments')
def rsi_201811_exists_and_loaded_sample_cis(_):
    collection_exercise_details.go_to('RSI', '201811')
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_scheduled(ce_state), ce_state
    collection_exercise_details.load_sample('resources/sample_files/business-survey-sample-date.csv')
    success_text = collection_exercise_details.get_sample_success_text()
    assert success_text == 'Sample loaded successfully'
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_201803_0001.xlsx')
    success_text = collection_exercise_details.get_collection_instrument_success_text()
    assert success_text == 'Collection instrument loaded'


@when('the user navigates to the survey details for RSI')
def navigate_to_rsi_details(_):
    collection_exercise.go_to('RSI')


@then('the status of the 201811 collection exercise is Ready for Review')
def rsi_201811_is_ready_for_review(_):
    collection_exercises = collection_exercise.get_collection_exercises()
    # Status updated async so wait until updated
    assert is_text_present_with_retry('Ready for review', 10)
    assert '201811' in (ce['exercise_ref'] for ce in collection_exercises)


@given('the user has loaded the sample')
@when('the user loads the sample')
def load_sample(_):
    collection_exercise_details.load_sample('resources/sample_files/business-survey-sample-date.csv')
    success_text = collection_exercise_details.get_sample_success_text()
    assert success_text == 'Sample loaded successfully'


@given('the user has loaded the collection instruments')
@when('the user loads the collection instruments')
def load_collection_instruments(_):
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_201803_0001.xlsx')
    success_text = collection_exercise_details.get_collection_instrument_success_text()
    assert success_text == 'Collection instrument loaded'


@then('the status of the collection exercise is Ready for Review')
def ce_details_state_is_ready_for_review(_):
    assert is_text_present_with_retry('Ready for review', 10)
