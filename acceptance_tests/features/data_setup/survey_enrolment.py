import traceback

from acceptance_tests.features.data_setup import setup_utilities


def scenario_setup_survey_enrolment(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError as e:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'Frontstage can see the survey they are enrolling in': setup_utilities.scenario_setup_not_defined,
    'Frontstage user can create an account': setup_utilities.scenario_setup_not_defined
}
