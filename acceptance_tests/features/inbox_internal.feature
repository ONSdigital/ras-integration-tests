Feature: Internal inbox
  As an internal user
  I need to view all inbox messages
  So that I can work on the messages as required

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: If there are no messages the user will be informed of this.
    Given the user has access to secure messaging
    When they navigate to the inbox messages
    Then they are informed that there are no messages

  Scenario: User is able to view all Inbox messages.
    Given the user has access to secure messaging
      And the secure message database is populated with messages
    When they navigate to the inbox messages
    Then they are able to view all received messages
