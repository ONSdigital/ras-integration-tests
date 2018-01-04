from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise


@given('the 2017 collection exercise for the BRES survey exists')
def bres_2017_exists(_):
    pass


@when('the internal user views the 2017 collection exercise for the BRES survey')
def internal_user_views_2017_bres_collection_exercise(_):
    collection_exercise.go_to('bres', 'BRES_2017')


@then('the internal user can view the collection exercise details')
def internal_user_can_view_bres_2017_collection_exercise_details(_):
    survey_info = collection_exercise.get_survey_info()
    assert survey_info == "221 - Business Register and Employment Survey (BRES)"
    period = collection_exercise.get_period()
    assert period == "BRES_2017"
    user_description = collection_exercise.get_user_description()
    assert user_description == "August 2017"