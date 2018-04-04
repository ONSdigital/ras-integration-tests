Feature: External inbox
  As an external user
  I need to view all inbox messages 
  So that I can work on the messages as required

  Background: The respondent is signed into their account
    Given the respondent is signed into their account

  @sm112_s01
  Scenario: User is able to view all Inbox messages
    Given the user has conversations in their list
    When they navigate to the inbox messages
    Then they are able to view a list of conversations

  @sm112_s02
  Scenario: User is able to view a preview of the latest message in a converstion
    Given the user has conversations in their list
    When they navigate to the inbox messages
    Then they are able to preview the first 80 characters (respecting word boundaries) of the latest message in the conversation

  @sm112_s03
  Scenario: User is able to view message details
    Given the user has conversations in their list
    When they navigate to the inbox messages
    Then the user will be able to view the conversation subject and the date and time the latest message was received

  @sm112_s04
  Scenario: User will be informed if there are no conversations in the list
    Given the user has no conversations to view
    When they navigate to the inbox messages
    Then they are informed of this

  @sm112_s05
  Scenario: User is able to distinguish unread messages in their inbox
    Given the user has no messages in their inbox
    When the user has an unread message in their inbox
    And they navigate to the inbox messages
    Then they are able to distinguish that the message is unread

