Feature: Internal inbox
  As an internal user
  I need to view all inbox messages
  So that I can work on the messages as required

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: User navigates to the surveys page from collection exercise
    Given the user has access to secure messaging
    When they navigate to the inbox messages
    Then they are informed that there are no messages
