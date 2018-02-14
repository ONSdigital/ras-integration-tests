from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 201803 collection exercise for the QIFDI survey has been created')
def qifdi_201803_exists(_):
    pass


@when('the internal user navigates to the collection exercise details page')
def given_internal_user_views_2017_bres_collection_exercise(_):
    collection_exercise_details.go_to('QBS', '1803')


@when('the user loads the sample')
def load_sample(_):
    collection_exercise_details.load_sample()
    success_text = collection_exercise_details.get_sample_success_text()
    assert success_text == 'Sample successfully loaded'


@when('the user loads the collection instruments')
def load_collection_instruments(_):
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_0001_201803.xlsx')
    success_text = collection_exercise_details.get_collection_instrument_success_text()
    assert success_text == 'Collection instrument loaded'


@then('the status of the collection exercise is Ready for Review')
def ce_details_state_is_ready_for_review():
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Ready for Review'
