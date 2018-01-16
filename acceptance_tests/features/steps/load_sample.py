from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@then('the user is able to load the sample')
def load_sample(_):
    collection_exercise_details.load_sample()
    success_text = collection_exercise_details.get_sample_success_text()
    assert success_text == 'Sample loaded'
