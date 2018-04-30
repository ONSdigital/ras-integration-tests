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
    Given the user has got messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view all received messages in reverse chronological order/latest first

  @sm139_s01
  Scenario: User is able to view a list of filter options
    Given the user has access to secure messaging
    When they navigate to the select survey page
    Then they are able to view a dropdown list of surveys

  @sm114_s01
  Scenario: User is able to distinguish unread messages in their inbox
    Given the user has no messages in their inbox
    When the user has an unread message in their inbox
    And they navigate to the inbox messages
    Then they are able to distinguish that the message is unread

  @sm114_s02
  Scenario: Messages are no longer distinguished as unread once they have been viewed
    Given the user has no messages in their inbox
    When the user has an unread message in their inbox
    And they navigate to the inbox messages
    And they view the unread message
    And they navigate to the inbox messages
    Then the message is no longer marked as unread

  @sm127_s01
  Scenario: User views 5 messages when 5 are there
    Given the user has no messages in their inbox
    And the user has got '5' messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view '5' messages

  @sm127_s02
  Scenario: User views 10 messages when 15 are there
    Given the user has no messages in their inbox
    And the user has got '15' messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view '10' messages
    And the pagination links are available
