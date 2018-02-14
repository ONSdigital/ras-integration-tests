from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 1803 collection exercise for the QBS survey has been created')
def qbs_1803_exists(_):
    pass


@given('the internal user navigates to the collection exercise details page for QBS 1803')
@when('the internal user navigates to the collection exercise details page for QBS 1803')
def internal_user_views_2017_bres_collection_exercise(_):
    collection_exercise_details.go_to('QBS', '1803')


@then('the user is able to view the status of the collection exercise')
def ce_details_state_is_displayed():
    ce_state = browser.find_by_id('ce_status').value
    assert ce_state != ''