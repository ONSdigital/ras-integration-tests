from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details, survey
from controllers.collection_exercise_controller import get_events_for_collection_exercise


MANDATORY_EVENTS = ['mps', 'go_live', 'return_by', 'reminder', 'exercise_end']


@given('the mandatory event dates collection exercise for 1803 exist')
def event_dates_exist(_):
    survey_id = '02b9c366-7397-42f7-942a-76dc5876d86d'  # QBS
    for event in MANDATORY_EVENTS:
        data = get_events_for_collection_exercise(survey_id, '1803', event)
        assert data['timestamp'] != ''


@when('the user navigates to the collection exercise details page for 1803')
@when('they navigate to the Collection Exercise Details Page')
def internal_user_views_ce_details(_):
    collection_exercise_details.go_to('QBS', '1803')


@then('the state of the collection exercise is Scheduled')
@then('they are able to see the Scheduled Status for that Collection Exercise')
def ce_details_state_is_scheduled(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Scheduled', ce_state
    events = collection_exercise_details.get_collection_exercise_events()
    assert all((value) for value in events.values())


@given('the user is on the Survey Page')
def user_on_survey_page(_):
    survey.go_to()


@given('the user is on the Survey Details Page')
@when('they navigate to the Survey Details page')
def user_navigate_to_survey_details(_):
    collection_exercise.go_to('QBS')


@then('they are able to see the Status for each collection exercise')
def survey_ce_state_is_scheduled(_):
    row = collection_exercise.get_table_row_by_period('1803')
    assert row['state'] == 'Scheduled', row['state']
