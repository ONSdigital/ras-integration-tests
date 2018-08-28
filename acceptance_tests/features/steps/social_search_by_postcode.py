from behave import given, when, then

from acceptance_tests.features.pages import social_search_by_postcode


@given('the SEL user receives a phone call from a respondent')
def internal_user_navigates_to_social_page(context):
    social_search_by_postcode.go_to()


@given('the user enters a postcode that doesnt exist in the sample')
def user_enters_postcode_that_doesnt_exist(context):
    internal_user_navigates_to_social_page(context)
    context.invalid_postcode = 'LN10 5GB'
    social_search_by_postcode.enter_postcode(context.invalid_postcode)


@when('they enter a postcode')
def user_enters_valid_postcode(_):
    social_search_by_postcode.enter_postcode('NP10 8XG')
    social_search_by_postcode.click_search_by_postcode()


@when('the internal user searches for that postcode')
def user_clicks_search(_):
    social_search_by_postcode.click_search_by_postcode()


@then('all address are returned for the postcode')
def return_addresses_for_searched_postcode(_):
    case_ref = social_search_by_postcode.get_reference_number()
    post_code = social_search_by_postcode.get_postcode()
    address_details = social_search_by_postcode.get_address()
    assert 'LMS100002' == case_ref, case_ref
    assert 'NP10 8XG' == post_code, post_code
    assert 'Office for National Statistics, Cardiff Road, Gwent District, Newport' in address_details, \
        address_details


@then('no postcodes/addresses are to be returned')
def do_not_return_addresses_for_partially_searched_postcode(context):
    empty_result = social_search_by_postcode.get_search_results()
    assert f'0 results found for {context.invalid_postcode}' in empty_result, empty_result
