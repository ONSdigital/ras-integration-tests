from behave import given, when, then


@given('The user has an active account and is assigned an username and password')
def sign_in(_):
    pass


@when('They enter the correct username and password')
def sign_in(_):
    pass


@when('They enter an incorrect username and / or password')
def sign_in(_):
    pass


@then('The user is directed to their home page?')
def sign_in(_):
    pass


@then('The user is notified that an error has occurred')
def sign_in(_):
    pass
