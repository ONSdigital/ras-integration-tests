from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 201803 collection exercise for the QIFDI survey has been created')
def qifdi_201803_exists(_):
    pass


@when('the internal user navigates to the collection exercise details page for QIFDI 201803')
def internal_user_views_collection_exercise(_):
    collection_exercise_details.go_to('QIFDI', '201803')


@then('the user is able to load the collection instruments')
def load_collection_instruments(_):
    collection_exercise_details.load_collection_instrument()
    success_text = collection_exercise_details.get_collection_instrument_success_text()
    assert success_text == 'Collection instrument loaded'
