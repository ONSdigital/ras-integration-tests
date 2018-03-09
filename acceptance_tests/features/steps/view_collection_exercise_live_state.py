import time

from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from controllers import collection_exercise_controller


@given('the user has confirmed that "{survey}" "{period}" is Ready for Live')
def internal_user_views_ready_for_live(_, survey, period):
    collection_exercise_details.go_to(survey, period)
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state), ce_state


@given('the user is on the "{survey}" Page')
@when('they navigate to the "{survey}" page')
def user_navigate_to_survey_details(_, survey):
    collection_exercise.go_to(survey)


@when('they navigate to the Collection Exercise Details Page for "{period}"')
def user_navigate_to_ce_details(_, period):
    collection_exercise.click_ce_link(period)


@when('"{survey}" "{period}" go live date hits')
def go_live_date_hits(_, survey, period):
    # PUT to force the scheduler
    s_id = {
        'rsi': '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c',
        'bricks': 'cb8accda-6118-4d3b-85a3-149e28960c54',
    }[survey.lower()]
    datetime = '2018-01-21T00:00:00.000Z'  # some time in the past
    collection_exercise_controller.update_event_for_collection_exercise(s_id, period, 'go_live', datetime)


@then('the state of a collection exercise is to be changed to Live')
@then('they are able to see the Live Status for that Collection Exercise')
def ce_details_state_is_live(_):
    ce_state = collection_exercise_details.get_status()
    for i in range(20):
        if collection_exercise.is_live(ce_state):
            break
        time.sleep(1)
        browser.reload()
        ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_live(ce_state), ce_state


@then('they are able to see the Live Status for "{period}"')
def survey_ce_state_is_live(_, period):
    ce_state = collection_exercise.get_table_row_by_period(period)['state']
    assert collection_exercise.is_live(ce_state), ce_state
