from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details


@when('the internal user navigates to the survey details page for QBS')
def internal_user_views_qbs(_):
    collection_exercise.go_to('QBS')


@then('the status of the collection exercise is listed as Scheduled')
def survey_ce_state_is_scheduled(_):
    row = collection_exercise.get_table_row_by_period('1803')
    assert row['state'] == 'Scheduled'


@then('the status of the collection exercise is displayed as Scheduled')
def ce_details_state_is_scheduled(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Scheduled'
