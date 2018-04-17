Feature: Reply to message internal
  As an internal user
  I need to be able to reply to a secure message
  So that I can respond to the external users messages

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @sm108_s01
  Scenario: User is able to reply to a message that they have been sent
    Given the internal user has received a message
    When they view the message
    Then they are able to reply

  @sm108_s02
  Scenario: user is able to enter text up to and including 10,000 characters in the body of the message
    Given the internal user has received a message
    When they view the message
    And they enter text in the body of the message
    Then they are able to enter free text up to and including 10,000 characters

  @sm108_s03
  Scenario: User is only able to send a reply if there is text in the body of the message
    Given the internal user has received a message
    When they view the message
    And they enter text in the body of the message
    Then they are able to reply

  @sm108_s04
  Scenario: The user is to be navigated to the inbox on replying to a message
    Given the internal user has received a message
    When they view the message
    And they reply to the message
    Then they are to be navigated to the inbox of messages

  @sm108_s05
  Scenario: When replying to a message, the user is to receive system feedback confirming the message has been sent
    Given the internal user has received a message
    When they view the message
    And they reply to the message
    Then they receive confirmation that the message has been sent
