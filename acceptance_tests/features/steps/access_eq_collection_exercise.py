from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.environment import enrol_respondent
from acceptance_tests.features.pages import surveys_todo
from config import Config
from controllers import party_controller


@given('the respondent has a CE for an eQ available')
def respondent_has_eq_ce_available(context):
    party_id = party_controller.get_party_by_email(Config.RESPONDENT_USERNAME)['id']
    # Enrolling for QBS 1806
    enrol_respondent(party_id, '02b9c366-7397-42f7-942a-76dc5876d86d', '1806')


@when('the respondent accesses the eQ CE')
def respondent_accesses_eq_ce(_):
    surveys_todo.go_to()
    surveys_todo.access_survey('Quarterly Business Survey')


@then('the respondent lands on the correct eQ Homepage for the survey and CE and CI')
def respondent_redirected_to_eq(_):
    url = browser.url
    assert 'https://eq-test/session?token=' in url, url
    token = url[30:]
    assert len(token.split('.')) == 5   # check correct jwt format
