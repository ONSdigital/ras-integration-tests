from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from controllers.collection_exercise_controller import post_event_to_collection_exercise


@when('the internal user navigates to the survey details page for QBS')
def internal_user_views_qbs(_):
    collection_exercise.go_to('QBS')


@then('the status of the collection exercise is listed as Scheduled')
def survey_ce_state_is_scheduled(_):
    row = collection_exercise.get_table_row_by_period('1803')
    assert row['state'] == 'Scheduled', row['state']


@then('the status of the collection exercise is displayed as Scheduled')
def ce_details_state_is_scheduled(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Scheduled', ce_state


@given('the 201806 collection exercise for the Bricks survey is Created')
def ce_details_state_is_created(_):
    collection_exercise_details.go_to('Bricks', '201806')
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Created', ce_state
    events = collection_exercise_details.get_collection_exercise_events()
    assert all(not(value) for value in events.values())


@when('the user loads the mandatory events')
def load_ce_events(_):
    # Manually adding the events until the functionality exists on the FE
    survey_id = 'cb8accda-6118-4d3b-85a3-149e28960c54'
    period = '201806'
    dates = ['2018-03-14T17:41:00.000Z', '2018-03-19T17:41:00.000Z', '2018-03-27T17:41:00.000Z', '2018-05-08T17:41:00.000Z', '2020-04-30T17:41:00.000Z']
    tags = ['mps', 'go_live', 'return_by', 'first_reminder', 'exercise_end']
    for tag, date_str in zip(tags, dates):
        post_event_to_collection_exercise(survey_id, period, tag, date_str)
    # Reload the page to see the new state
    collection_exercise_details.go_to('Bricks', '201806')
