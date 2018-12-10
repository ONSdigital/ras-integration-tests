@standalone
@business
Feature: External user recovering their password
  As an external user
  I need to sign in to the retrieve my password
  So that I can access my SDC account and carry out a number of actions

  Background: A respondent has to have locked themselves out of their account
    Given the respondent has locked themselves out of their account

  @fixture.setup.data.with.enrolled.respondent.user
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

  @fixture.setup.data.with.enrolled.respondent.user
  Scenario: User re-sends reset password link
    Given the user has clicked an expired password reset link
    And the user has been notified that the link they used has expired
    When they click the request new password link
    Then the user is notified that they should check their email

  @fixture.setup.data.with.enrolled.respondent.user
  Scenario: User clicks a reset password link
    Given the user has received a link to reset password
    When the user clicks the link
    Then the user is taken to a reset password form

  @fixture.setup.data.with.enrolled.respondent.user
  Scenario: User attempts to reset password with incorrect confirmed password
    Given the user has clicked a valid password reset link
    When the user enters a new password and an incorrect confirmed password
    And they submit the new password
    Then the user is notified that the passwords don't match

  @fixture.setup.data.with.enrolled.respondent.user
  Scenario: User attempts to reset password with password not meeting requirements
    Given the user has clicked a valid password reset link
    When the user enters and confirms a new password which does not meet requirements
    And they submit the new password
    Then the user is notified that the password does not meet requirements

  @fixture.setup.data.with.enrolled.respondent.user
  Scenario: User attempts to reset password
    Given the user has clicked a valid password reset link
    When the user enters a new password and confirms the password
    And they submit the new password
    Then the user is notified that the password has been changed

  @fixture.setup.data.with.enrolled.respondent.user
  Scenario: User logs in with new password
    Given the user has reset their password
    When the user enters their new credentials
    Then they successfully log in to their account
