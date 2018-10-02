@social
Feature: Internal user signs in to social UI
  As an internal user
  I need to sign in to the social SDC system
  So that I can access my SDC account and carry out a number of actions

  Scenario: User signs in correctly (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter the correct username and password (social)
    Then the user is directed to their home page (social)

  Scenario: User attempts sign in with incorrect username and receives authentication error (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter an incorrect username and correct password (social)
    Then the user is notified that an authentication error has occurred (social)

  Scenario: User attempts sign in with incorrect password and receives authentication error (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter a correct username and incorrect password (social)
    Then the user is notified that an authentication error has occurred (social)

  Scenario: User attempts sign in and receives authentication error (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter an incorrect username and password (social)
    Then the user is notified that an authentication error has occurred (social)

  Scenario: User attempts sign in and is notified that they are required to enter a password (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter a correct username and no password (social)
    Then the user is notified that a password is required (social)

  Scenario: User attempts sign in and is notified that they are required to enter a username (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter no username and a correct password (social)
    Then the user is notified that a username is required (social)

  Scenario: User attempts sign in and is notified that they are required to enter a username and password (social)
    Given the user has an active account and is assigned a username and password (social)
    When they enter no username and no password (social)
    Then the user is notified that a username and password is required (social)
