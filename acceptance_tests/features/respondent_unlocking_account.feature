Feature: Respondent unlocking their account
  As a respondent
  I need to unlock my account, if I exceed 10 failed sign in attempts
  So that I can access my account

  Background: A respondent has to have created an account
    Given The respondent has created an account which is unverified called "locked1@email.com"
    And The respondent has created an account which is verified called "locked2@email.com"

  Scenario: Unverified user is informed if they exceed 10 failed sign in attempts
    Given "locked1@email.com" enters their password incorrectly 10 times in a row
    Then The system is to inform the user that an email has been sent to a registered email

  Scenario: User is sent an email after 10 failed sign in attempts, gets directed to the password reset page
    Given An unverified user has received the unsuccessful sign in email
    When "locked1@email.com" clicks the link
    Then They are directed to the reset password page

  Scenario: Account is unlocked and verified after confirming password reset
    Given An Unverified user's account is locked
    And The user has entered a new password and confirmed the password
    When They submit the new password
    Then Their password is reset and their account is unlocked and verified

  Scenario: Verified user is informed if they exceed 10 failed sign in attempts
    Given "locked2@email.com" enters their password incorrectly 10 times in a row
    Then The system is to inform the user that an email has been sent to a registered email

  Scenario: User is sent an email after 10 failed sign in attempts
    Given A verified user has received the unsuccessful sign in email
    When "locked2@email.com" clicks the link
    Then They are directed to the reset password page

  Scenario: Account is unlocked after confirming password reset
    Given A verified user's account is locked
    And The user has entered a new password and confirmed the password
    When They confirm their password reset
    Then Their password is reset and their account is unlocked and verified
