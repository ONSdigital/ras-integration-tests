Feature: Internal user signs in
  As an internal user
  I need to sign in to the SDC system
  So that I can access my SDC account and carry out a number of actions


  Scenario: User signs in correctly
    Given The user has an active account and is assigned a username and password
    When They enter the correct username and password
    Then The user is directed to their home page

  Scenario: User attempts sign in and receives authentication error
    Given The user has an active account and is assigned a username and password
    When They enter an incorrect username and correct password
    Then The user is notified that an authentication error has occurred

  Scenario: User attempts sign in and receives authentication error
    Given The user has an active account and is assigned a username and password
    When They enter a correct username and incorrect password
    Then The user is notified that an authentication error has occurred

  Scenario: User attempts sign in and receives authentication error
    Given The user has an active account and is assigned a username and password
    When They enter an incorrect username and password
    Then The user is notified that an authentication error has occurred

  Scenario: User attempts sign in and is notified that they are required to enter a password
    Given The user has an active account and is assigned a username and password
    When They enter a correct username and no password
    Then The user is notified that a password is required

  Scenario: User attempts sign in and is notified that they are required to enter a username
    Given The user has an active account and is assigned a username and password
    When They enter no username and a correct password
    Then The user is notified that a username is required

  Scenario: User attempts sign in and is notified that they are required to enter a username and password
    Given The user has an active account and is assigned a username and password
    When They enter no username and no password
    Then The user is notified that a username is required
    And The user is notified that a password is required
