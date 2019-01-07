from behave import given, then, when

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit
from acceptance_tests.features.pages.respondent_unlocking_account import get_lockout_message, locking_respondent_out


@given('a respondent locks their account')
def respondent_account(context):
    locking_respondent_out(username=context.respondent_email)


@then('the account will be locked')
def check_account_locked_externally(_):
    assert get_lockout_message()


@then('the internal user can see that the respondent has an account status locked')
@then('there is also an unlock link below the locked')
def check_account_locked_internally(context):
    reporting_unit.go_to(context.short_name)
    reporting_unit.click_data_panel(context.short_name)
    assert browser.find_by_id('account-status')[0].value == 'Locked'
    assert browser.find_by_id('respondent-unlock-link')[0].value == 'Unlock'


@when('an internal user clicks on the unlock link')
def unlock_account_internally(context):
    reporting_unit.click_data_panel(context.short_name)
    browser.find_by_id('respondent-unlock-link')[0].click()


@when('they confirm the unlock')
def confirm_unlock_account_internally(_):
    browser.find_by_id('confirm-btn').click()


@then('the reporting unit page is reloaded with a change flag')
@then('account status for the respondent is showing as active')
def account_status_changed(context):
    assert browser.find_by_id('success')[0].value == 'Account status changed'
    reporting_unit.click_data_panel(context.short_name)
    assert browser.find_by_id('account-status')[0].value == 'Active'
