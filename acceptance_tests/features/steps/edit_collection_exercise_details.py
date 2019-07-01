from datetime import date, timedelta

from behave import then, when

from acceptance_tests.features.pages import collection_exercise, \
    collection_exercise_details, \
    edit_collection_exercise_details_form
from common.browser_utilities import wait_for


@when('they request to edit/amend collection exercise details')
def navigate_to_edit_collection_exercise_details_page(_):
    collection_exercise_details.click_edit_collection_exercise_period_button()


@when('they edit the collection exercise details')
def edit_collection_exercise_details(context):

    period = date.today() + timedelta(days=365)
    context.expected_period = period.strftime("%Y%m")
    context.expected_user_description = period.strftime("%d %B %Y")

    edit_collection_exercise_details_form.edit_period(context.expected_period)
    # Line below _temporarily removed_ until temporary ticket to remove editing is reversed.
    # edit_collection_exercise_details_form.edit_user_description(context.expected_user_description)
    edit_collection_exercise_details_form.click_save()


@when('the state is at/after Ready for live')
def check_collection_exercise_state(_):
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state)


@then('the collection exercise details match the updated values')
def view_updated_collection_exercise_details(context):

    collection_exercises = wait_for(fn=collection_exercise.get_collection_exercises, timeout=15, retry_after=3)

    assert collection_exercises[0]['exercise_ref'] == context.expected_period
    assert collection_exercises[0]['user_description'] == context.expected_user_description


@then('they cannot edit the collection exercise period')
def edit_period_icon_disappears_if_period_cannot_be_edited(_):
    assert not collection_exercise_details.check_edit_period_is_enabled()
