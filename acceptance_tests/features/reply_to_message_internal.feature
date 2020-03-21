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
