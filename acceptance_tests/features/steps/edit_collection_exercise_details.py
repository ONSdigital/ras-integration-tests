from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import edit_collection_exercise_details_form, collection_exercise_details, \
    collection_exercise


@given('the internal user is on the collection exercise details page')
def check_user_on_collection_exercise_details_page(_):
    collection_exercise_details.go_to('RSI', '201808')
    assert "023 RSI 201808 | Surveys | Survey Data Collection" in browser.title


@given('the internal user is on the collection exercise details page for RSI 201812')
def check_user_on_collection_exercise_details_page_for_rsi_201812(_):
    collection_exercise_details.go_to('QBS', '1809')
    assert "139 QBS 1809 | Surveys | Survey Data Collection" in browser.title


@when('they request to edit/amend collection exercise details')
def navigate_to_edit_collection_exercise_details_page(_):
    collection_exercise_details.click_edit_collection_exercise_period_button()


@when('they edit/amend the details')
def edit_collection_exercise_details(_):
    edit_collection_exercise_details_form.edit_period('201906')
    edit_collection_exercise_details_form.edit_user_description('12 June 2019')
    edit_collection_exercise_details_form.click_save()


@when('the state is at/after Ready for live')
def check_collection_exercise_state(_):
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state)


@then('they can view the updated details')
def view_updated_collection_exercise_details(context):
    collection_exercises = collection_exercise.get_collection_exercises()
    for row in context.table:
        collection_exercises_by_period = next(filter(lambda ce: ce['exercise_ref'] == row['period'],
                                                     collection_exercises))
        assert collection_exercises_by_period['exercise_ref'] == "201906"
        assert collection_exercises_by_period['user_description'] == "12 June 2019"


@then('they cannot edit the collection exercise period')
def edit_period_icon_disappears_if_period_cannot_be_edited(_):
    assert not collection_exercise_details.check_edit_period_is_enabled()
