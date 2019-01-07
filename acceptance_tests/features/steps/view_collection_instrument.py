from behave import given, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the collection instruments have been loaded')
def collection_instruments_loaded(_):
    pass


@then('they are able to see the filename of all collection instruments that have been loaded')
def should_see_loaded_ci(_):
    cis = collection_exercise_details.get_collection_instruments()
    assert 'test_collection_instrument.xlxs' in cis[0]
