from behave import given, then, when

from acceptance_tests import browser
from acceptance_tests.features.pages import forgotten_password_respondent, reporting_unit
from acceptance_tests.features.pages.forgotten_password_respondent import get_password_reset_url
from acceptance_tests.features.pages.respondent_unlocking_account import get_lockout_message, locking_respondent_out, \
    respondent_password_reset_complete


@given('the respondent has locked themselves out of their account')
def respondent_unverified_account(context):
    locking_respondent_out(context.respondent_email)


@given('they click the password reset link')
@when('they click the password reset link')
def user_clicks_password_reset_link(context):
    browser.visit(get_password_reset_url(context))


@given('the respondent enters their password incorrectly 10 times in a row')
def locking_respondent_out_of_account(context):
    locking_respondent_out(context.respondent_email)


@given('the internal user navigates to locked accounts RU page')
@when('the internal user navigates to locked accounts RU page')
def enter_locked_accounts_ru_ref(context):
    reporting_unit.go_to(context.short_name)


@then('the system is to inform the user that an email has been sent to a registered email')
@given('an unverified user has received the unsuccessful sign in email')
@given('a verified user has received the unsuccessful sign in email')
def lock_out_page(_):
    assert get_lockout_message()


@then('they are directed to the reset password page')
def get_password_reset_page(_):
    assert forgotten_password_respondent.get_reset_password_message()


@given('an Unverified user\'s account is locked')
@given('a verified user\'s account is locked')
def users_account_is_locked(_):
    pass


@then('their password is reset and their account is unlocked and verified')
def password_reset_complete(_):
    assert respondent_password_reset_complete()


@when('they confirm their password reset')
def submitting_password(_):
    forgotten_password_respondent.click_confirm_new_password()


@when('they click the unlock button')
@given('they have clicked the unlock button')
def click_unlock(_):
    browser.find_by_id('respondent-unlock-link').click()


@when('they click confirm unlock account')
def click_unlock_account(_):
    browser.find_by_id('confirm-btn').click()


@when('they click cancel on the unlock account screen')
def click_cancel_unlock_screen(_):
    browser.find_by_id('cancel').click()


@then('they are redirected and "Account status changed" displayed to user')
def account_status_changed_msg(_):
    assert browser.find_by_text('Account status changed')
