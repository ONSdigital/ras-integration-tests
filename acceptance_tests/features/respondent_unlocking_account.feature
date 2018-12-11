@standalone
@business
@fixture.setup.data.with.unverified.respondent.user
Feature: Respondent unlocking their account
  As a respondent
  I need to unlock my account, if I exceed 10 failed sign in attempts
  So that I can access my account

  Background: A respondent has to have created an account
    Given the respondent has locked themselves out of their account

  Scenario: Unverified user is informed if they exceed 10 failed sign in attempts
    Then The system is to inform the user that an email has been sent to a registered email

  Scenario: User is sent an email after 10 failed sign in attempts, gets directed to the password reset page
    Given an unverified user has received the unsuccessful sign in email
    When they click the password reset link
    Then they are directed to the reset password page

  Scenario: Account is unlocked and verified after confirming password reset
    Given an unverified user has received the unsuccessful sign in email
    And they click the password reset link
    When the user enters a new password and confirms the password
    And they submit the new password
    Then their password is reset and their account is unlocked and verified
