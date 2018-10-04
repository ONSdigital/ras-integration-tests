from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit
from acceptance_tests.features.pages.respondent_unlocking_account import create_locked_account,\
    get_lockout_message


@given('a respondent with an email "{username}" locks their account')
def respondent_account(_, username):
    create_locked_account(username=username)


@then('the account will be locked')
def check_account_locked_externally(_):
    assert get_lockout_message(_)


@then('the internal user can see that the respondent has an account status locked')
@then('there is also an unlock link below the locked')
def check_account_locked_internally(_):
    reporting_unit.go_to('49900000005')
    reporting_unit.click_data_panel('Bricks')
    assert browser.find_by_id('account-status')[0].value == 'Locked'
    assert browser.find_by_id('respondent-unlock-link')[0].value == 'Unlock'


@given('an internal user clicks on the unlock link')
def unlock_account_internally(_):
    browser.find_by_id('respondent-unlock-link')[0].click()


@when('they confirm the unlock')
def confirm_unlock_account_internally(_):
    browser.find_by_id('confirm-btn').click()


@then('the reporting unit page is reloaded with a change flag')
@then('account status for the respondent is showing as active')
def account_status_changed(_):
    assert browser.find_by_id('success')[0].value == 'Account status changed'
    reporting_unit.click_data_panel('Bricks')
    assert browser.find_by_id('account-status')[0].value == 'Active'
