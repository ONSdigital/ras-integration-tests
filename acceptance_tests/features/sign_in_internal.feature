@business
@standalone
@fixture.setup.with.internal.user
Feature: Internal user signs in
  As an internal user
  I need to sign in to the SDC system
  So that I can access my SDC account and carry out a number of actions

  Scenario: User signs in correctly
    Given the user has an active account and is assigned a username and password
    When they enter the correct username and password
    And they click the sign in button
    Then the user is directed to their home page

  Scenario: User attempts sign in with incorrect username and receives authentication error
    Given the user has an active account and is assigned a username and password
    When they enter an incorrect username and correct password
    And they click the sign in button
    Then the user is notified that an authentication error has occurred

  Scenario: User attempts sign in with incorrect password and receives authentication error
    Given the user has an active account and is assigned a username and password
    When they enter a correct username and incorrect password
    And they click the sign in button
    Then the user is notified that an authentication error has occurred

  Scenario: User attempts sign in and receives authentication error
    Given the user has an active account and is assigned a username and password
    When they enter an incorrect username and password
    And they click the sign in button
    Then the user is notified that an authentication error has occurred

  @skip
  Scenario: User attempts sign in and is notified that they are required to enter a password
    Given the user has an active account and is assigned a username and password
    When they enter a correct username and no password
    And they click the sign in button
    Then the user is notified that a password is required

  @skip
  Scenario: User attempts sign in and is notified that they are required to enter a username
    Given the user has an active account and is assigned a username and password
    When they enter no username and a correct password
    And they click the sign in button
    Then the user is notified that a username is required

  @skip
  Scenario: User attempts sign in and is notified that they are required to enter a username and password
    Given the user has an active account and is assigned a username and password
    When they click the sign in button
    Then the user is notified that a username and password is required
