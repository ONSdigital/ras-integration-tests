from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 1803 collection exercise for the QBS survey has been created')
def bres_2017_exists(_):
    pass


@when('the internal user navigates to the collection exercise details page')
def internal_user_views_2017_bres_collection_exercise(_):
    collection_exercise_details.go_to('QBS', '1803')


@then('the user is able to view the survey details and period for that survey')
def internal_user_can_view_bres_2017_collection_exercise_details(_):
    ce_details = collection_exercise_details.get_collection_exercise_details()
    assert ce_details['survey_info'] == "139 - Quarterly Business Survey (QBS)"
    assert ce_details['period'] == "1803"
    assert ce_details['user_description'] == "9 March 2018"
