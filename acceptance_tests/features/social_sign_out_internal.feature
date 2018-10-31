@social
@standalone
Feature: Internal user signs out from social
  As an internal user
  I need to sign out of the social SDC system
  So that I can secure my account

  Scenario: User signs out (social)
    Given the internal user is already signed in to social UI
    When they click the sign out link (social)
    Then the user is logged out and shown the sign in page and they see a successfully signed out message (social)
