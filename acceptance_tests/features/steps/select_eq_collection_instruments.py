from behave import when, then

from acceptance_tests.features.pages import collection_exercise_details


@when('the user selects the collection instrument')
def select_eq_ci(_):
    collection_exercise_details.add_eq_ci()


@then('the collection instrument is added into the collection exercise')
def eq_ci_linked_to_ce(_):
    success_text = collection_exercise_details.get_success_panel_text()
    assert success_text == 'Collection instruments added'
