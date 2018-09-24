from behave import given


@given('a social survey exists')
def create_social_survey(_):
    pass


def scenario_setup_users_are_able_to_view_their_case_details(_):
    pass


def scenario_setup_user_needs_to_be_able_to_search_for_a_case_by_postcode(_):
    pass


def scenario_setup_user_is_to_be_informed_if_we_do_not_hold_the_postcode_that_has_been_entered(_):
    pass


def feature_setup_social_survey(context):
    scenarios[context.scenario_name](context)


# Add each Scenario name + data setup method handler here
scenarios = {
    'Users are able to view their case details': scenario_setup_users_are_able_to_view_their_case_details,
    'User needs to be able to search for a case by postcode': scenario_setup_user_needs_to_be_able_to_search_for_a_case_by_postcode,
    'User is to be informed if we do not hold the postcode that has been entered': scenario_setup_user_is_to_be_informed_if_we_do_not_hold_the_postcode_that_has_been_entered
}
