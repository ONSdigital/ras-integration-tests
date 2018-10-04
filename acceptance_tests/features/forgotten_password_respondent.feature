Feature: External user recovering their password
  As an external user
  I need to sign in to the retrieve my password
  So that I can access my SDC account and carry out a number of actions

  Background: A respondent has to have created an account
    Given The respondent has created an account which is unverified called "unverified1@email.com"

  Scenario: User attempts to sign in and has forgotten their password
    Given The user has an active account and they have forgotten their password
    When They enter a registered email address
    Then The user is notified that they have had a password reset link email sent to them

  Scenario: User attempts to sign in and has forgotten their password attempting to reset with it with an invalid email
    Given The user has an active account and they have forgotten their password
    When They enter a invalid email address
    Then The user is notified that a valid email address is required

  Scenario: User attempts to sign in and has forgotten their password attempting to reset with it with an unregistered email
    Given The user has an active account and they have forgotten their password
    When They enter a unregistered email address
    Then The user is notified that they have had a password reset link email sent to them

  Scenario: User attempts to reset password with an expired link
    Given The user has received an expired link for the reset password form
    When They click a expired link
    Then The user is notified that the link has expired
    And Can now request a new link

  Scenario: User re-sends reset password link
    Given The user has been notified that the link they used has expired
    When They click the request new password link
    Then The user is notified that they should check their email

  Scenario: User clicks a reset password link
    Given A user has received a link to reset password
    When "unverified1@email.com" clicks the link
    Then The user is taken to a reset password form

  Scenario: User attempts to reset password with incorrect confirmed password
    Given The user has entered a new password and an incorrect confirmed password
    When They submit the new password
    Then The user is notified that the passwords don't match

  Scenario: User attempts to reset password with password not meeting requirements
    Given The user has entered a new password and confirmed the password which does not meet requirements
    When They submit the new password
    Then The user is notified that the password does not meet requirements

  Scenario: User attempts to reset password
    Given The user has entered a new password and confirmed the password
    When They submit the new password
    Then The user is notified that the password has been changed

  Scenario: User logs in with new password
    Given The user has reset their password
    When  "unverified1@email.com" enters their credentials
    Then They successfully log in to their account
