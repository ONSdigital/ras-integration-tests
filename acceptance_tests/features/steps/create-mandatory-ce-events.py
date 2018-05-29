from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, create_collection_exercise


@given('the internal has created a new collection exercise for {survey} and period {period} with shown as {user_description}')
def create_new_collection_exercise(_, survey, period, user_description):
    collection_exercise.go_to(survey)
    collection_exercise.click_create_ce_link()
    create_collection_exercise.edit_period(period)
    create_collection_exercise.edit_user_description(user_description)
    create_collection_exercise.click_save()

@when("there is no mandatory event dates scheduled for the ce for {period}")
def check_no_mandatory_event_set(_, period):
    
