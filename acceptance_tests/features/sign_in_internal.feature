Feature: Internal user signs in
  As an internal user
  I need to sign in to the SDC system
  So that I can access my SDC account and carry out a number of actions

  Background: Internal user is already signed in
    Given The internal user is already signed in

  Scenario: User signs in correctly
    Given The user has an active account and is assigned an username and password
    When They enter the correct username and password
    Then The user is directed to their home page?

  Scenario: User attempts sign in and receives error
    Given The user has an active account and is assigned an username and password
    When They enter an incorrect username and/or password
    Then The user is notified that an error has occurred
