from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 2017 collection exercise for the BRES survey has been created')
def bres_2017_exists(_):
    pass


@given('the 2017 collection exercise events for the BRES survey has been created')
def bres_2017_events_exist(_):
    pass


@when('the internal user navigates to the collection exercise details page')
def internal_user_views_2017_bres_collection_exercise(_):
    collection_exercise_details.go_to('bres', 'BRES_2017')


@then('the user is able to view the survey details and period for that survey')
def internal_user_can_view_bres_2017_collection_exercise_details(_):
    ce_details = collection_exercise_details.get_collection_exercise_details()
    assert ce_details['survey_info'] == "221 - Business Register and Employment Survey (BRES)"
    assert ce_details['period'] == "221_201712"
    assert ce_details['user_description'] == "August 2017"


@then('the user is able to view the event dates for that collection exercise')
def internal_user_can_view_bres_2017_collection_exercise_events(_):
    ce_events = collection_exercise_details.get_collection_exercise_events()
    assert ce_events['mps'] == "Mon 11 Sep 2017 23:00 GMT"
    assert ce_events['go_live'] == "Mon 11 Sep 2017 23:00 GMT"
    assert ce_events['return_by'] == "Sun 06 Oct 2018 00:00 GMT"
    assert ce_events['first_reminder'] == "???"
    assert ce_events['exercise_end'] == "Fri 29 Jun 2018 23:00 GMT"
