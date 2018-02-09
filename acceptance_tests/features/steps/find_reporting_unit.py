from behave import given, when, then

from acceptance_tests.features.pages import reporting_units


@given('the internal user navigates to the find RU page')
def given_internal_user_on_find_ru_page(_):
    reporting_units.go_to_find_ru()


@when('the internal user enters a RU Ref')
def internal_user_enters_ru_ref(_):
    reporting_units.search_reporting_unit('49900000005')


@then('the Reporting Unit is displayed back to the user')
def internal_user_presented_with_correct_ru(_):
    rus = reporting_units.get_reporting_units()
    assert '49900000005' in rus and 'OFFICE FOR NATIONAL STATISTICS' in rus


@when('the internal user enters a RU Name')
def internal_user_enters_ru_name(_):
    reporting_units.search_reporting_unit('Office for national statistics')
