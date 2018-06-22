@secure_messaging
Feature: Internal user to send message
  As an internal ONS user
  I need to be able to send a secure message
  So that I can query data that has been received

  Background: User already logged in
    Given the internal user is already signed in
    And The internal user has found the associated respondent

  @sm101_s01
  Scenario: 'To' field will be pre-populated with respondent name (up to 100 characters)
    When they choose to send them a secure message and navigated to the 'send message' page
    Then the 'To' field is populated with the respondent's name

  @sm101_s02
  Scenario: User is able to enter free text in the subject field up to and including 96 characters
    Given the user is on the send message page
    When they enter text in the subject of the message
    Then they are able to enter free text up to and including 96 characters

  @sm101_s03
  Scenario: User is able to enter free text  in the body of the message up to and including 10,000 characters
    Given the user is on the send message page
    When they enter text in the body of the message
    Then they are able to enter free text up to and including 10,000 characters

  @sm101_s04
  Scenario: User is only able to send a message if there is text in the body of all fields ('Subject' and 'Message')
    Given the user is on the send message page
    When they enter text in the subject and body of the message
    Then they are able to send the message

  @sm101_s05
  Scenario: The user is to be able to cancel out of sending a message (and navigated back to where they came from)
    Given the user is on the send message page
    When they choose to cancel out of sending a message
    Then they are navigated back to the page in which they navigated from

  @sm101_s06
  Scenario: On sending the message the user is to be navigated to the inbox
    Given the user is on the send message page
    And the user has entered text in the subject and body of the message
    When they select send
    Then they are navigated to the inbox of messages

  @sm101_s07
  Scenario: On sending the message the user is to receive confirmation that the message has been sent
    Given the user is on the send message page
    And the user has sent a secure message
    When they are navigated to the inbox of messages
    Then they are presented with confirmation that the message has been sent
