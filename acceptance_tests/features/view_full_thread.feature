Feature: View conversation thread
  As an internal user
  I need to see all of the previous messages in a conversation
  So that I have the full context for my reply

  Background: Internal user is already signed in
    Given the internal user is already signed in


  @sm124_s01
  Scenario: The user select one conversation from the inbox.
    Given An internal user has conversations in their inbox
    When  The internal user selects a conversation
    Then  the internal user can see all messages in the conversation

  @sm124_s02
  Scenario: The date and time of messages should be visible in each item of the conversation
    Given An internal user has conversations in their inbox
    When  The internal user selects a conversation
    Then  The internal user can see the date and time for each message in the conversation

  @sm124_s03
  Scenario: User is able to differentiate between ONS messages and external messages in a conversation
    Given An internal user has conversations in their inbox
    When  The internal user selects a conversation
    Then  The internal user can see which messages have been sent by ONS users and which are an external users messages


  @sm124_s04
  Scenario: Opening a conversation, the user is taken to the latest message in that conversation
    Given An internal user has conversations in their inbox
    When  The internal user selects a conversation
    Then  They are taken to the latest message in that conversation
