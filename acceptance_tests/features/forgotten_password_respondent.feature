Feature: External user recovering their password
  As an external user
  I need to sign in to the retrieve my password
  So that I can access my SDC account and carry out a number of actions

  Background: A respondent has to have created an account
    Given the respondent has created an account which is unverified called "unverified1@email.com"

  Scenario: User attempts to sign in and has forgotten their password
    Given the user has an active account and they have forgotten their password
    When they enter a registered email address
    Then the user is notified that they have had a password reset link email sent to them

  Scenario: User attempts to sign in and has forgotten their password attempting to reset with it with an invalid email
    Given the user has an active account and they have forgotten their password
    When they enter a invalid email address
    Then the user is notified that a valid email address is required

  Scenario: User attempts to sign in and has forgotten their password attempting to reset with it with an unregistered email
    Given the user has an active account and they have forgotten their password
    When they enter a unregistered email address
    Then the user is notified that they have had a password reset link email sent to them

  Scenario: User attempts to reset password with an expired link
    Given the user has received an expired link for the reset password form
    When they click a expired link
    Then the user is notified that the link has expired
    And can now request a new link

  Scenario: User re-sends reset password link
    Given the user has been notified that the link they used has expired
    When they click the link the request new reset password link
    Then the user is notified that they should check their email

  Scenario: User clicks a reset password link
    Given a user has received a link to reset password
    When "unverified1@email.com" clicks the link
    Then the user is taken to a reset password form

  Scenario: User attempts to reset password with incorrect confirmed password
    Given the user has entered a new password and an incorrect confirmed password
    When they submit the new password
    Then the user is notified that a that the passwords don't match

  Scenario: User attempts to reset password with password not meeting requirements
    Given the user has entered a new password and confirmed the password which does not meet requirements
    When they submit the new password
    Then the user is notified that a that the password does not meet requirements

  Scenario: User attempts to reset password
    Given the user has entered a new password and confirmed the password
    When they submit the new password
    Then the user is notified that a that the password has been changed
