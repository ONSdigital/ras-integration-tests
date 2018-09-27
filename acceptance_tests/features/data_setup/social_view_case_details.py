import traceback

from acceptance_tests.features.data_setup import setup_utilities


def scenario_setup_social_view_case_details(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError as e:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'Users are able to view their case details': setup_utilities.scenario_setup_not_defined
}
