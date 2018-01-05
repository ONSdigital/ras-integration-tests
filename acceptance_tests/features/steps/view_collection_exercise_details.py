from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 2017 collection exercise for the BRES survey has been created')
def bres_2017_exists(_):
    pass


@when('the internal user navigates to the collection exercise details page')
def internal_user_views_2017_bres_collection_exercise(_):
    collection_exercise_details.go_to('bres', 'BRES_2017')


@then('the user is able to view the survey details and period for that survey')
def internal_user_can_view_bres_2017_collection_exercise_details(_):
    ce_details = collection_exercise_details.get_collection_exercise_details()
    assert ce_details['survey_info'] == "221 - Business Register and Employment Survey (BRES)"
    assert ce_details['period'] == "BRES_2017"
    assert ce_details['user_description'] == "August 2017"
