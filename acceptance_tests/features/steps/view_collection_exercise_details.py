from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 1803 collection exercise for the QBS survey has been created')
def qbs_1803_exists(_):
    pass


@given('the 1803 collection exercise events for the QBS survey has been created')
def qbs_2018_events_exist(_):
    pass


@given('the internal user navigates to the collection exercise details page for QBS 1803')
@when('the internal user navigates to the collection exercise details page for QBS 1803')
def internal_user_views_qbs_2018_collection_exercise(_):
    collection_exercise_details.go_to('QBS', '1803')


@then('the user is able to view the survey details and period for that survey')
def internal_user_can_view_qbs_2018_collection_exercise_details(_):
    ce_details = collection_exercise_details.get_collection_exercise_details()
    assert ce_details['survey_info'] == "139 QBS"
    assert ce_details['survey_title'] == "Quarterly Business Survey"
    assert ce_details['period'] == "1803"
    assert ce_details['user_description'] == "9 March 2018"


@then('the user is able to view the event dates for that collection exercise')
def internal_user_can_view_qbs_2018_collection_exercise_events(_):
    ce_events = collection_exercise_details.get_collection_exercise_events()
    assert ce_events['mps'] == "Wednesday 14 Mar 2018 00:00"
    assert ce_events['go_live'] == "Monday 19 Mar 2018 00:00"
    assert ce_events['return_by'] == "Tuesday 27 Mar 2018 01:00"
    assert ce_events['first_reminder'] == "Tuesday 03 Apr 2018 01:00"
    assert ce_events['exercise_end'] == "Thursday 30 Apr 2020 01:00"


@then('the user is able to view the variable event dates for that collection exercise')
def internal_user_can_view_qbs_2018_collection_exercise_variable_event_dates(_):
    ce_events = collection_exercise_details.get_collection_exercise_events()
    assert ce_events['ref_period_start'] == "Friday 09 Mar 2018"
    assert ce_events['ref_period_end'] == "Saturday 31 Mar 2018"
    assert ce_events['employment'] == "Friday 09 Mar 2018"
    assert ce_events['second_reminder'] == "Monday 23 Apr 2018 01:00"
    assert ce_events['third_reminder'] == "Saturday 05 May 2018 01:00"
