Feature: Internal inbox
  As an internal user
  I need to view all inbox messages
  So that I can work on the messages as required

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @sm111_s01
  Scenario: If there are no messages the user will be informed of this.
    Given the user has access to secure messaging
    And the user has no messages in their inbox
    When they navigate to the inbox messages
    Then they are informed that there are no messages

  @sm111_s02
  Scenario: User is able to view all Inbox messages.
    Given the user has got messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view all received messages

  @sm111_s03
  Scenario: User is able to view all the following details
    Given the user has access to secure messaging
    When they navigate to the inbox messages
    Then they are able to view the RU Ref, Subject, From, To, Date and time for each message

  @sm111_s04
  Scenario: User is able to view all the following details
    Given the user has access to secure messaging
    When they navigate to the inbox messages
    Then they are able to view all received messages in reverse chronological order/latest first
