from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 201803 collection exercise for the ASHE survey has been created')
def ashe_201803_exists(_):
    pass


@when('the internal user navigates to the collection exercise details page for ASHE survey')
def go_to_ashe(context):
    collection_exercise_details.go_to(context.short_name, context.period)


@then('the user is able to load the ASHE sample file')
def load_ashe_sample_file(_):
    collection_exercise_details.load_sample('resources/sample_files/us081-load_ashe_sample_file/ashe_sample.csv')
    assert collection_exercise_details.get_sample_success_text()
