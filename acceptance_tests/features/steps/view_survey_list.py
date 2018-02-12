from behave import given, then

from acceptance_tests.features.pages.surveys_todo import get_collection_exercise_periods


@given('the go live event for the collection exercise has passed')
@given('the go live event for the collection exercise has not passed')
def default_pass(context):
    pass


@then('the respondent is displayed that collection exercise')
def respondent_views_bricks_201801(context):
    ce_periods = get_collection_exercise_periods()
    for period in ce_periods:
        assert period.value == 'January 2018'


@then('the respondent is not displayed that collection exercise')
def respondent_cant_view_bricks_201812(context):
    ce_periods = get_collection_exercise_periods()
    for period in ce_periods:
        assert period.value != 'December 2018'
