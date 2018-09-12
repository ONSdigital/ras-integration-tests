from common.survey_utilities import *

logger = wrap_logger(getLogger(__name__))

# Add scenario names here
valid_scenario_names = {
    'make a request for a new code': True,
    'display an unused active code': True,
    'frontstage can see the survey they are enrolling in': True,
    'frontstage user can create an account': True
}


def is_valid_scenario_name(actual_scenario_name, expected_scenario_name):
    key_scenario_name = actual_scenario_name.lower()

    try:
        return valid_scenario_names[key_scenario_name] and actual_scenario_name == expected_scenario_name
    except KeyError:
        logger.exception('Invalid scenario name', scenario_name=actual_scenario_name)
        raise Exception(f'Invalid scenario name "{actual_scenario_name}"')


def is_display_an_unused_active_code_scenario(scenario_name):
    return is_valid_scenario_name(scenario_name.lower(), 'display an unused active code')


def is_generate_new_enrolment_code_scenario(scenario_name):
    return is_valid_scenario_name(scenario_name.lower(), 'make a request for a new code')


def is_frontstage_can_see_the_survey_they_are_enrolling_in_scenario(scenario_name):
    return is_valid_scenario_name(scenario_name.lower(), 'frontstage can see the survey they are enrolling in')


def is_frontstage_user_can_create_an_account_scenario(scenario_name):
    return is_valid_scenario_name(scenario_name.lower(), 'frontstage user can create an account')
