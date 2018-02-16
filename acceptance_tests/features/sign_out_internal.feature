Feature: Internal user signs out
  As an internal user
  I need to sign out of the SDC system
  So that I can secure my account

  Scenario: User signs out
    Given the internal user is already signed in
    When they click the sign out link
    Then the user is logged out and shown the sign in page and they see a successfully signed out message
