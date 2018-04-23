Feature: External User Views a Conversation
  As an external User
  I need to be able to see all of the previous messages in a conversation
  So that I have the full context for my reply

  Background: Respondent already logged in
    Given the respondent is signed into their account

  @sm128_s01
  Scenario: User needs to be able to view all of the previous messages in a conversation
    Given an external user has sent ONS a message
    When an internal user responds
    Then the external user can see all messages in the conversation

  @sm128_s02
  Scenario: The date and time of messages should be visible in each item of the conversation
    Given an external user has sent ONS a message
    When an internal user responds
    Then the external user can see the date and time for each message in the conversation

  @sm128_s03
  Scenario: When opening a conversation, the user is taken to the latest message in that conversation
    Given the external user has a conversation
    When they view that conversation
    Then they are taken to the latest message in that conversation (external)

  @sm128_s04
  Scenario: User is able to differentiate between ONS messages and external messages in a conversation
    Given an external user has sent ONS a message
    When an internal user responds
    Then the external user can see which messages have been sent by ONS and which ones they have sent

  @sm128_s05
  Scenario: User is able to reply to the latest item in a conversation
    Given the external user has a conversation
    When they view that conversation
    Then they are able to reply (external)

  @sm128_s06
  Scenario: The reply will be sent to the relevant team for that survey
    Given the external user has a conversation
    When they reply in that conversation
    Then the reply will be sent to the correct team

  @sm128_s07
  Scenario: User is able to enter text up to and including 10,000 characters in the body of the message
    Given the external user has a conversation
    When they reply in that conversation
    Then they are able able to enter up to and including 10,000 characters in the body of their reply

  @sm128_s08
  Scenario: User is only able to reply to a conversation if there is text in the body of their reply.
    Given the external user has a conversation
    When they enter text into the body of their reply (external)
    Then they are able to reply to the conversation

  @sm128_s09
  Scenario: The user is to be navigated to the list on replying to a conversation
    Given the external user has a conversation
    When they reply in that conversation
    Then they are to be navigated back to the list of conversations

  @sm128_s10
  Scenario: When the user has sent their reply, they receive system feedback confirming the message has been sent
    Given the external user has a conversation
    When they reply in that conversation
    Then they receive confirmation that the message has been sent (external)
