@business
@standalone
@secure_messaging
@fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
Feature: Internal user to send message
  As an internal ONS user
  I need to be able to send a secure message
  So that I can query data that has been received

  Background: User already logged in
    Given the internal user is already signed in
    And The internal user has found the associated respondent

  @sm101_s01
  Scenario: 'To' field will be pre-populated with respondent name (up to 100 characters)
    When they choose to send them a secure message and navigated to the send message page
    Then the To field is populated with the respondent's name

  @sm101_s06
  Scenario: On sending the message the user is to be navigated to the inbox
    Given the user is on the send message page
    And the user has entered text in the subject and body of the message
    When they select send
    Then they are navigated to the inbox of messages
    