@business
@standalone
@secure_messaging
@fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
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

  @sm123_s01
  Scenario: User is able to close a conversation
    Given the user has no messages in their inbox
    And the internal user has received a message
    When they view the message
    And they close the conversation
    Then they receive confirmation that the conversation is closed
    And the conversation appears in their closed list

  @sm123_s02
  Scenario: User is able to reopen a closed conversation
    Given the internal user has a closed conversation in their inbox
    When they view the closed message
    And they reopen the conversation
    Then they receive confirmation that the conversation has been reopened
    And the conversation is not present in their closed list
    And the conversation is present in their open list

  @sm123_s05
  Scenario: User is able to see messages in the conversation in reverse chronological order (latest first)
    Given the internal user has a conversation in their inbox
    When they view the message
    Then they are able to see the messages in the conversation in chronological order

  @sm599_s01
  Scenario: When closing a conversation the user should be returned to the same page
    Given the user has got '30' messages in their inbox
    And the internal user opens first message on page '2'
    When they close the conversation
    Then they are taken back to page '2'
    And they receive confirmation that the conversation is closed

  @sm599_s02
  Scenario: When closing the only conversation on the final page the user should be returned to the new final page
    Given the user has got '21' messages in their inbox
    And the internal user opens first message on page '3'
    When they close the conversation
    Then they are taken back to page '2'
    And they receive confirmation that the conversation is closed
