from behave import given, then

from acceptance_tests.features.pages.surveys_todo import get_collection_exercise_periods


@given('the go live event for the collection exercise has passed')
@given('the go live event for the collection exercise has not passed')
def default_pass(context):
    pass


@then('the respondent is displayed that collection exercise')
def respondent_views_bricks_201801(context):
    ce_periods = get_collection_exercise_periods()
    ce_period_values = [ce.value for ce in ce_periods]
    assert 'January 2018' in ce_period_values


@then('the respondent is not displayed that collection exercise')
def respondent_cant_view_bricks_201812(context):
    ce_periods = get_collection_exercise_periods()
    ce_period_values = [ce.value for ce in ce_periods]
    assert 'December 2018' not in ce_period_values
