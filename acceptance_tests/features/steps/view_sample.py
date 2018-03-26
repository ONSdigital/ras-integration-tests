from behave import given, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the user has loaded the sample in context of 1803 collection exercise for the QBS')
def given_user_has_loaded_a_sample_for_qbs_1803(_):
    collection_exercise_details.go_to('QBS', '1803')
    collection_exercise_details.load_sample('resources/sample_files/business-survey-sample-date.csv')


@then('the user is able to view the sample loaded for that collection exercise')
def then_the_user_is_able_to_view_loaded_sample(_):
    sample = collection_exercise_details.get_loaded_sample()
    assert 'Total businesses' in sample
    assert 'Collection instruments' in sample
    assert '1' in sample
