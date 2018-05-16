@secure_messaging
Feature: Send message from todo list
  As a Respondent
  I need to be able to send a secure message in relation to an RU and a survey in my todo list
  So that my query can be dealt with by the relevant team

  Background: Respondent already logged in
    Given the respondent is signed into their account

  @sm137-01
  Scenario: Able to send a message in relation to each survey on todo list
    When the respondent navigates to their surveys todo list
    Then the respondent is able to send a message

  @sm137-02
  Scenario: Respondent is navigated to create message page when choosing to send message on todo list
    Given the respondent is on their todo list
    When the respondent chooses to send a message for a specific RU and survey
    Then the respondent is navigated to the create message page

  @sm137-03
  Scenario: The message is to be sent to a selected survey team mailbox
    Given the respondent is sending a message in relation to bricks
    When the respondent enters a valid message
    Then the message will be sent to the internal Bricks mailbox

  @sm137-04
  Scenario: Subject field can be max 96 characters long
    Given the respondent chooses to send a message to ONS
    When the respondent enters more than 96 characters in the subject field
    And selects to send message
    Then an error message appears specifying subject too long

  @sm137-05
  Scenario: Body field can be max 10000 characters long
    Given the respondent chooses to send a message to ONS
    When the respondent enters more than 10000 characters in the body field
    And selects to send message
    Then an error message appears specifying body too long

  @sm137-06
  Scenario: Body and Subject fields must be populated
    Given the respondent chooses to send a message to ONS
    When the respondent tries to send the message without populating the body and subject fields
    Then an error message appears specifying body and subject fields are required

  @sm137-08
  Scenario: Respondent receives confirmation message is sent
    Given the respondent chooses to send a message to ONS
    When the respondent enters a valid message
    And the message is sent
    Then the respondent is navigated to their inbox and notified message sent successfully

  @sm137-09
  Scenario: Subject field must be populated
    Given the respondent chooses to send a message to ONS
    When the respondent populates the body field but not the subject
    And chooses to send the message
    Then an error message appears specifying subject must be populated

  @sm137-10
  Scenario: Body field must be populated
    Given the respondent chooses to send a message to ONS
    When the respondent populates the subject field but not the body field
    And selects to send message
    Then an error message appears notifying the respondent a body must be supplied