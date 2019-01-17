@business
@standalone
@secure_messaging
@fixture.setup.data.with.enrolled.respondent.user.and.internal.user
Feature: View conversation thread
  As an internal user
  I need to see all of the previous messages in a conversation
  So that I have the full context for my reply

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @sm124_s01
  Scenario: The user select one conversation from the inbox.
    Given An internal user has conversations in their inbox
    When The internal user selects a conversation
    Then the internal user can see all messages in the conversation

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

  Scenario: Opening a conversation, the user is taken to the latest message in that conversation and can see mark as unread
    Given the internal user has received a message
    When  they view the message
    Then  They can see mark as unread

  Scenario: Marking unread internal user is taken to conversation view
    Given the internal user has received a message
    When  they view the message
     And  they select mark unread
    Then  they are taken to conversation view
     And  the expected message is displayed
     And  they are able to distinguish that the message is unread

  Scenario: Message sent from internal, respondent replies , user who sent original message can mark as unread
    Given the internal user has received a message
      And  an internal user responds and respondent signs in
      And the respondent navigates to their inbox
      And the respondent replies to first conversation
    When The internal user is already signed in
      And the internal person views the message
      Then  They can see mark as unread
     

  Scenario: Message sent from internal, respondent replies , user different to who sent original message can not mark as unread
    Given the internal user has received a message
      And  an internal user responds and respondent signs in
      And the respondent navigates to their inbox
      And the respondent replies to first conversation
    When an alternate internal user signs in
      And the internal person views the message
      Then  They cannot see mark as unread

  Scenario: Message sent to group user opens message and clicks back , message marked as read
    Given the internal user has received a message
    When  the internal person views the message
      And the user selects back
    Then  the message is no longer marked as unread
    
    
  Scenario: Message sent from internal, respondent replies , user who sent original opens and selects back, message marked as read
    Given the internal user has received a message
      And  an internal user responds and respondent signs in
      And the respondent navigates to their inbox
      And the respondent replies to first conversation
    When The internal user is already signed in
      And the internal person views the message
      And the user selects back
    Then  the message is no longer marked as unread

  Scenario: Message sent from internal, respondent replies , user different to who sent original opens and selects back, message not marked as read
    Given the internal user has received a message
      And  an internal user responds and respondent signs in
      And the respondent navigates to their inbox
      And the respondent replies to first conversation
    When an alternate internal user signs in
      And the internal person views the message
      And the user selects back
    Then  they are able to distinguish that the message is unread
