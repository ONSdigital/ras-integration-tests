Feature: External user recovering their password
  As an external user
  I need to sign in to the retrieve my password
  So that I can access my SDC account and carry out a number of actions

  Scenario: User attempts to sign in and has forgotten their password
    Given the user has an active account and they have forgotten their password
    When they enter a registered email address
    Then the user is notified that they have had a password reset link email sent to them

  Scenario: User attempts to sign in and has forgotten their password attempting to reset with it with an invalid email
    Given the user has an active account and they have forgotten their password
    When they enter a invalid email address
    Then the user is notified that a valid email address is required