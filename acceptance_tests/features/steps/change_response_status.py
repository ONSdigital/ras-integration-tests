from behave import when, given, then

from config import Config
from acceptance_tests.features.pages import change_response_status, surveys_history
from controllers.collection_exercise_controller import get_collection_exercise
from controllers.database_controller import get_iac_for_collection_exercise_and_ru_ref
from controllers.party_controller import get_party_by_email, add_survey
from controllers.survey_controller import get_survey_by_shortname


@given('the survey for 49900000004 has been completed by phone')
def survey_for_49900000004_completed_by_phone(_):
    # Add additional survey for 49900000002 for enrolled respondent
    survey_id = get_survey_by_shortname('Bricks').get('id')
    collection_exercise_id = get_collection_exercise(survey_id, '201801').get('id')
    enrolment_code = get_iac_for_collection_exercise_and_ru_ref(collection_exercise_id, '49900000004')
    party_id = get_party_by_email(Config.RESPONDENT_USERNAME).get('id')
    add_survey(party_id, enrolment_code)


@when('the internal user changes the response status from \'Not started\' to \'Completed by phone\'')
def internal_user_changes_response_status(_):
    change_response_status.update_response_status('COMPLETED_BY_PHONE')


@when('the respondent goes to the history page')
def respondent_goes_to_history_page(_):
    surveys_history.go_to_history_tab()


@then('the survey for 49900000004 has the status completed by phone')
def survey_for_49900000002_has_status_completed_by_phone(_):
    status = surveys_history.get_status_text()
    assert status == 'Completed by phone'
