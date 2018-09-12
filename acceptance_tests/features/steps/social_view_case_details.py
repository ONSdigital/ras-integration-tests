from behave import given, when, then

from acceptance_tests.features.pages import social_view_case_details, social_search_by_postcode


@given('SEL searches for a postcode')
def internal_user_searches_for_postcode(context):
    social_search_by_postcode.go_to()
    social_search_by_postcode.enter_postcode(context.address["postcode"])
    social_search_by_postcode.click_search_by_postcode()


@when('they select the address')
def internal_user_selects_the_address(context):
    social_search_by_postcode.click_case_link()


@then('they can see all the above case details')
def internal_sel_user_can_view_social_case_details(context):
    actual_social_ref_number = social_view_case_details.get_reference_number()
    actual_social_status = social_view_case_details.get_status()
    actual_social_address = social_view_case_details.get_address()

    assert f'{context.address["TLA"]}{context.address["reference"]}' == \
           actual_social_ref_number, actual_social_ref_number
    assert 'Not started' == actual_social_status, actual_social_status
    assert context.address["address_line1"] == actual_social_address['address_line_1'], \
        actual_social_address['address_line_1']
    assert context.address["address_line2"] == actual_social_address['address_line_2'], \
        actual_social_address['address_line_2']
    assert context.address["locality"] == actual_social_address['locality'], \
        actual_social_address['locality']
    assert context.address["town_name"] == actual_social_address['town'], \
        actual_social_address['town']
    assert context.address["postcode"] == actual_social_address['postcode'], \
        actual_social_address['postcode']
