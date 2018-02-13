from behave import given, when, then

from acceptance_tests import browser
from config import Config
from controllers.collection_exercise_controller import get_survey_collection_exercises


@given('the collection exercises for that survey exist')
def ce_exist_for_survey():
    bricks_id = 'cb8accda-6118-4d3b-85a3-149e28960c54'
    collection_exercises = get_survey_collection_exercises(bricks_id)
    assert len(collection_exercises) != 0


@when('the internal user navigates to survey details page')
@given('the internal user is on the survey details page')
def view_survey_details():
    browser.visit('{}/surveys/{}'.format(Config.RESPONSE_OPERATIONS_UI, 'Bricks'))


@then('the state of the collection exercise is created')
def survey_ce_state_is_created(context):
    for row in context.table:
        if row['period'] == '201801':
            assert row['status'] == 'Created'


@given("the internal user is on the survey's page")
def view_surveys():
    browser.visit('{}/surveys'.format(Config.RESPONSE_OPERATIONS_UI))


@then('the internal user is able to see the status for each collection exercise')
def all_ce_have_states(context):
    for row in context.table:
        assert row['status'] is not None


@when('the internal user navigate to the collection exercise details page')
def view_ce_details():
    browser.visit('{}/surveys/{}/{}'.format(Config.RESPONSE_OPERATIONS_UI, 'Bricks', '201801'))


@then('the displayed status should be Created')
def ce_details_state_is_created():
    ce_state = browser.find_by_id('ce_status').value
    assert ce_state == 'Created'
