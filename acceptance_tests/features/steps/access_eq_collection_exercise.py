from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import surveys_todo
from common.collection_exercise_utilities import enrol_respondent
from config import Config
from controllers import party_controller


@given('the respondent has a CE for an eQ available')
def respondent_has_eq_ce_available(context):
    surveys_todo.go_to()


@when('the respondent accesses the eQ CE')
def respondent_accesses_eq_ce(context):
    surveys_todo.access_survey(context.long_name)


@then('the respondent is redirected to eQ with a token')
def respondent_redirected_to_eq(_):
    url = browser.url
    assert 'https://eq-test/session?token=' in url, url
    token = url.partition('token=')[2]
    assert len(token.split('.')) == 5   # check correct jwt format
