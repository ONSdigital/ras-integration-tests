from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_collection_exercise, collection_exercise, survey


@given('internal user wants to create a collection exercise')
@given('internal user is creating a CE for a specific survey')
@given('internal user is creating a collection exercise')
def check_user_is_on_survey_page(_):
    collection_exercise.go_to('RSI')
    assert "RSI | Surveys | Survey Data Collection" in browser.title


@then('they click create collection exercise')
@when('they click create collection exercise')
def click_create_collection_exercise(_):
    collection_exercise.click_create_ce_link()


@when('they enter period details that is in use by an existing collection exercise')
def user_enters_conflicting_period_data(_):
    create_collection_exercise.edit_period('201807')
    create_collection_exercise.edit_user_description('Duplicate period test')
    create_collection_exercise.click_save()


@when('they complete the required fields and save')
def user_creates_a_collection_exercise(_):
    create_collection_exercise.edit_period('202001')
    create_collection_exercise.edit_user_description('1 January 2020')
    create_collection_exercise.click_save()


@when('they have created the CE')
def user_creates_another_collection_exercise(_):
    create_collection_exercise.edit_period('202002')
    create_collection_exercise.edit_user_description('1 February 2020')
    create_collection_exercise.click_save()


@when('they enter details into the period field')
def user_enters_over_6_digits(_):
    create_collection_exercise.edit_period('1234567')
    create_collection_exercise.edit_user_description('1 January 2020')


@when('the collection exercise is created')
def collection_exercise_is_created(_):
    assert collection_exercise.get_collection_exercise_created_banner()


@then('they are taken to the collection exercise list for that survey')
def check_new_collection_exercise_exists(_):
    collection_exercise.click_collection_exercise_created_banner()
    assert "023 RSI 202001 | Surveys | Survey Data Collection" in browser.title


@then('the CE must be associated to the specific survey')
def check_new_collection_exercise_is_associated_to_the_survey(_):
    collection_exercise.click_collection_exercise_created_banner()
    assert "023 RSI 202002 | Surveys | Survey Data Collection" in browser.title


@then('they are asked to use different details')
@then('they are presented with an error screen')
def check_for_failed_validation(_):
    assert create_collection_exercise.period_error_panel()


@then('they can only enter a maximum of six characters')
def check_period_you_can_only_enter_6_characters(_):
    assert len(create_collection_exercise.check_period_length()) <= 6
