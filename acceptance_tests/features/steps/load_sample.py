from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@then('the user is able to load the sample')
def load_sample(_):
    collection_exercise_details.load_sample('resources/sample_files/business-survey-sample-date.csv')
    success_text = collection_exercise_details.get_sample_success_text()
    assert success_text == 'Sample loaded successfully'


@when('the user selects a sample')
def internal_user_selects_sample(_):
    collection_exercise_details.select_sample('resources/sample_files/business-survey-sample-date.csv')


@then('the user is presented with sample details')
def internal_user_presented_with_sample_details(_):
    assert collection_exercise_details.has_sample_preview()


@given('the user is presented with sample details')
def given_internal_user_presented_with_sample_details(context):
    collection_exercise_details.go_to(context.short_name, context.period)
    collection_exercise_details.select_sample('resources/sample_files/business-survey-sample-date.csv')
    assert collection_exercise_details.has_sample_preview()


@when('the user cancels the sample')
def internal_user_cancels_the_sample(_):
    collection_exercise_details.cancel_sample_preview()


@then('the sample details are reset')
def sample_details_are_reset(_):
    assert not collection_exercise_details.has_sample_preview()
