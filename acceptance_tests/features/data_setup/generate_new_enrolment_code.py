import traceback

from common import respondent_utilities


def scenario_setup_make_a_request_for_a_new_code(context):
    user_name = respondent_utilities.make_respondent_user_name(str(context.unique_id), context.survey_short_name)
    respondent_id = \
        respondent_utilities.create_respondent(user_name=user_name, enrolment_code=context.iac)['id']
    respondent_utilities.create_respondent_user_login_account(user_name)
    respondent_utilities.enrol_respondent(respondent_id)


def scenario_setup_generate_new_enrolment_code(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'Make a request for a new code': scenario_setup_make_a_request_for_a_new_code
}
