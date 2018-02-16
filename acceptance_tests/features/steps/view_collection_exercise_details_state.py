from behave import then

from acceptance_tests.features.pages import collection_exercise_details


@then('the user is able to view the status of the collection exercise')
def ce_details_state_is_displayed(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state != ''
