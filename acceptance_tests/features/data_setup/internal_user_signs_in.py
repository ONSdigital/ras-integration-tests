import traceback

from acceptance_tests.features.data_setup import setup_utilities


def scenario_setup_internal_user_signs_in(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'User signs in correctly': setup_utilities.scenario_data_setup_not_required,
    'User attempts sign in with incorrect username and receives authentication error': setup_utilities.scenario_data_setup_not_required,
    'User attempts sign in with incorrect password and receives authentication error': setup_utilities.scenario_data_setup_not_required,
    'User attempts sign in and receives authentication error': setup_utilities.scenario_data_setup_not_required,
    'User attempts sign in and is notified that they are required to enter a password': setup_utilities.scenario_data_setup_not_required,
    'User attempts sign in and is notified that they are required to enter a username': setup_utilities.scenario_data_setup_not_required,
    'User attempts sign in and is notified that they are required to enter a username and password': setup_utilities.scenario_data_setup_not_required
}
