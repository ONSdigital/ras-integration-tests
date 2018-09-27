import traceback

from acceptance_tests.features.data_setup import setup_utilities


def scenario_setup_social_find_case_by_postcode(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError as e:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'User needs to be able to search for a case by postcode': setup_utilities.scenario_setup_not_defined,
    'User is to be informed if we do not hold the postcode that has been entered': setup_utilities.scenario_setup_not_defined
}
