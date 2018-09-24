from behave import given, when, then

from acceptance_tests.features.pages.respondent_unlocking_account import creating_unverified_account, \
    respondent_enters_wrong_password, get_lockout_message


@given('the respondent has created an account which is unverified')
def respondent_account(_):
    creating_unverified_account(username='unverified@test.com')


@given('A unverified user enters an incorrect password')
def respondent_invalid_login(_):
    respondent_enters_wrong_password(_)


@when('They enter a password incorrectly for the 10th time')
def locking_respondent_out(_):
    for i in range(0, 9):
        respondent_enters_wrong_password(_)


@then('The system is to inform the user that an email has been sent to a registered email')
def lock_out_page(_):
    assert get_lockout_message(_)