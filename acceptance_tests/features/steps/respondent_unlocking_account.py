from behave import given, when, then

from acceptance_tests.features.pages import forgotten_password_respondent
from acceptance_tests.features.pages.respondent_unlocking_account import creating_unverified_account,\
    get_lockout_message, respondent_password_reset_complete, locking_respondent_out
from acceptance_tests.features.steps.edit_respondent_details import create_respondent


@given('the respondent has created an account which is unverified called "{username}"')
def respondent_unverified_account(_, username):
    creating_unverified_account(username=username)


@given('the respondent has created an account which is verified called "{username}"')
def respondent_account(_, username):
    create_respondent(username)


@given('"{username}" enters their password incorrectly 10 times in a row')
def locking_respondent_out_of_account(_, username):
    locking_respondent_out(username)


@then('The system is to inform the user that an email has been sent to a registered email')
@given('An unverified user has received the unsuccessful sign in email')
@given('A verified user has received the unsuccessful sign in email')
def lock_out_page(_):
    assert get_lockout_message(_)


@then('They are directed to the reset password page')
def get_password_reset_page(_):
    assert forgotten_password_respondent.get_reset_password_message()


@given('An Unverified user\'s account is locked')
@given('A verified user\'s account is locked')
def users_account_is_locked(_):
    pass


@then('Their password is reset and their account is unlocked and verified')
def password_reset_complete(_):
    assert respondent_password_reset_complete()


@when('They confirm their password reset')
def submitting_password(_):
    forgotten_password_respondent.click_confirm_new_password()
