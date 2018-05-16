@secure_messaging
Feature: External conversations
  As an external user
  I need to view all external conversations
  So that I can work on the messages as required

  Background: The respondent is signed into their account
    Given the respondent is signed into their account

  @sm112_s01
  Scenario: User will be informed if there are no conversations in the list
    Given the external user has no conversations to view
    When they navigate to the external inbox messages
    Then they are informed that there are no external conversations

  @sm112_s02
  Scenario: User is able to view all messages
    Given the external user has conversations in their list
    When they navigate to the external inbox messages
    Then they are able to view a list of external conversations

  @sm112_s03
  Scenario: User is able to view a preview of the latest message in a conversation
    Given the external user has conversations in their list
      And they receive a message body with over 80 characters
    When they navigate to the external inbox messages
    Then they are able to preview the first 80 characters (respecting word boundaries) of the latest message in the conversation

  @sm112_s04
  Scenario: User is able to view message details
    Given the external user has conversations in their list
    When they navigate to the external inbox messages
    Then the user will be able to view the conversation subject and the date and time the latest message was received

  @sm112_s05
  Scenario: User is able to distinguish unread messages in their inbox
    Given the external user has conversations in their list
    When they navigate to the external inbox messages
    Then they are able to distinguish that the external message is unread

