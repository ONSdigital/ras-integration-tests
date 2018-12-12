from behave import given, then, when

from acceptance_tests.features.pages import collection_exercise_details
from controllers.collection_exercise_controller import convert_event_for_datetime, convert_event_for_date


@given('the 1803 collection exercise for the QBS survey has been created')
def qbs_1803_exists(_):
    pass


@given('a collection exercise exists')
def collection_exercise_exists(_):
    pass


@given('the internal user navigates to the collection exercise details page for QBS 1803')
@when('the internal user navigates to the collection exercise details page for QBS 1803')
def internal_user_views_qbs_2018_collection_exercise(_):
    collection_exercise_details.go_to('QBS', '1803')


@then('the user is able to view the survey details and period for that survey')
def internal_user_can_view_collection_exercise_details(context):
    expected_survey_info = f'{context.survey_ref} {context.short_name}'
    expected_survey_title = context.long_name
    expected_period = context.period
    expected_user_description = context.user_description

    actual_ce_details = collection_exercise_details.get_collection_exercise_details()
    assert actual_ce_details['survey_info'] == expected_survey_info
    assert actual_ce_details['survey_title'] == expected_survey_title
    assert actual_ce_details['period'] == expected_period
    assert actual_ce_details['user_description'] == expected_user_description


@then('the user is able to view the event dates for that collection exercise')
def internal_user_can_view_collection_exercise_events(context):
    dates = context.dates

    expected_mps = convert_event_for_datetime(dates['mps'])
    expected_go_live = convert_event_for_datetime(dates['go_live'])
    expected_return_by = convert_event_for_datetime(dates['return_by'])
    expected_first_reminder = convert_event_for_datetime(dates['first_reminder'])
    expected_exercise_end = convert_event_for_datetime(dates['exercise_end'])

    actual_ce_details = collection_exercise_details.get_collection_exercise_events()

    assert actual_ce_details['mps'] == expected_mps
    assert actual_ce_details['go_live'] == expected_go_live
    assert actual_ce_details['return_by'] == expected_return_by
    assert actual_ce_details['first_reminder'] == expected_first_reminder
    assert actual_ce_details['exercise_end'] == expected_exercise_end


@then('the user is able to view the variable event dates for that collection exercise')
def internal_user_can_view_collection_exercise_variable_event_dates(context):
    dates = context.dates

    expected_ref_period_start = convert_event_for_date(dates['go_live'])
    expected_ref_period_end = convert_event_for_date(dates['return_by'])
    expected_employment = convert_event_for_date(dates['employment'])
    expected_second_reminder = convert_event_for_datetime(dates['second_reminder'])
    expected_third_reminder = convert_event_for_datetime(dates['third_reminder'])

    actual_ce_details = collection_exercise_details.get_collection_exercise_events()

    assert actual_ce_details['ref_period_start'] == expected_ref_period_start
    assert actual_ce_details['ref_period_end'] == expected_ref_period_end
    assert actual_ce_details['employment'] == expected_employment
    assert actual_ce_details['second_reminder'] == expected_second_reminder
    assert actual_ce_details['third_reminder'] == expected_third_reminder
