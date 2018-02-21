from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the user has checked the contents of the collection exercise and it is all correct')
def user_checks_ce_contents(_):
    collection_exercise_details.go_to('RSI', '201812')
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
    collection_exercise_details.set_ready_for_live()
    success_text = collection_exercise_details.get_execution_success()
    assert success_text == 'Collection exercise executed'


@then('the collection exercise state is changed to Ready for Live')
def view_ready_for_live(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Ready for Live'
