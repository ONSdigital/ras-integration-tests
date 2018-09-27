import traceback

from acceptance_tests.features.data_setup import setup_utilities


def scenario_setup_social_disable_uac(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError as e:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'The user is able to change the status of a case': setup_utilities.scenario_setup_not_defined
}
