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
    And the respondents and messages have been created
    When they navigate to the inbox messages
    Then they are able to view all received messages

  Scenario: User is able to view all the following details
    Given the user has access to secure messaging
    When they navigate to the inbox messages
    Then they are able to view the RU Ref, Subject, From, To, Date/Time for each message

  Scenario: User is able to view all the following details
    Given the user has access to secure messaging
    When they navigate to the inbox messages
    Then they are able to view all received messages in reverse chronological order/latest first
