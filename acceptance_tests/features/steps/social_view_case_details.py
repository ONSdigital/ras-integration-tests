from behave import given, when, then

from acceptance_tests.features.pages import social_view_case_details, social_search_by_postcode


@given('SEL searches for a postcode')
def internal_user_searches_for_postcode(context):
    social_search_by_postcode.go_to()
    social_search_by_postcode.enter_postcode('NP10 8XG')
    social_search_by_postcode.click_search_by_postcode()


@when('they select the address')
def internal_user_selects_the_address(context):
    social_search_by_postcode.click_case_link()


@then('they can see all the above case details')
def internal_sel_user_can_view_social_case_details(context):
    actual_social_ref_number = social_view_case_details.get_reference_number()
    actual_social_status = social_view_case_details.get_status()
    actual_social_address = social_view_case_details.get_address()

    assert 'LMS100002' == actual_social_ref_number, actual_social_ref_number
    assert 'Not started' == actual_social_status, actual_social_status
    assert 'Office for National Statistics' == actual_social_address['address_line_1']
    assert 'Cardiff Road' == actual_social_address['address_line_2']
    assert 'Gwent District' == actual_social_address['locality']
    assert 'Newport' == actual_social_address['town']
    assert 'NP10 8XG' == actual_social_address['postcode']
