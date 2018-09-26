Feature: Respondent unlocking their account
  As a respondent
  I need to unlock my account, if I exceed 10 failed sign in attempts
  So that I can access my account

  Background: A respondent has to have created an account
    Given the respondent has created an account which is unverified called "unverified1@test.com"

  @us204_01
  Scenario: User is informed if they exceed 10 failed sign in attempts
    Given A unverified user enters an incorrect password
    When They enter a password incorrectly for the 10th time
    Then The system is to inform the user that an email has been sent to a registered email

  @us204_02
  Scenario: User is sent an email after 10 failed sign in attempts
    Given A verified user has received the unsuccessful sign in email
    When They click the reset password link
    Then They are directed to the reset password page

  @us204_03
  Scenario: User is sent an email after 10 failed sign in attempts
    Given An unverified user has received the unsuccessful sign in email
    When They click the reset password link
    Then They are directed to the reset password page

  @us204_04
  Scenario: Account is unlocked after confirming password reset
    Given A verified user's account is locked
    When They confirm their password reset
    Then Their password is reset and their account is unlocked

  @us204_05
  Scenario: Account is unlocked and verified after confirming password reset
    Given An Unverified user's account is locked
    When They confirm their password reset
    Then Their password is reset and their account is unlocked and verified