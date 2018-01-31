Feature: Internal user signs out
  As an internal user
  I need to sign out of the SDC system
  So that I can secure my account

  Background: Internal user is already signed in
    Given The internal user is already signed in

  Scenario: User signs out
    When They click the sign out link
    Then The user is logged out and shown the homepage
