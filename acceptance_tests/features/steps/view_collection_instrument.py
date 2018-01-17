from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the collection instruments have been loaded')
def load_collection_instruments(_):
    collection_exercise_details.go_to('QIFDI', '201803')
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_0001_201803.xlsx')


@when('the user navigates to the collection exercise details page')
def internal_user_views_collection_instruments(_):
    collection_exercise_details.go_to('QIFDI', '201803')


@then('they are able to see the filename of all collection instruments that have been loaded')
def should_see_loaded_ci(_):
    cis = collection_exercise_details.get_collection_instruments()
    assert '064_0001_201803.xlsx' in cis
