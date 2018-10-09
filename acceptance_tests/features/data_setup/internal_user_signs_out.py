import traceback

from acceptance_tests.features.data_setup import setup_utilities


def scenario_setup_internal_user_signs_out(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'User signs out': setup_utilities.scenario_data_setup_not_required
}
