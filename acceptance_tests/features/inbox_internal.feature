@business
@standalone
@secure_messaging
Feature: Internal inbox
  As an internal user
  I need to view all inbox messages
  So that I can work on the messages as required

  Background: Internal user is already signed in
    Given the internal user is already signed in


  @sm111_s03
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
  Scenario: User is able to view all the following details
    Given the user has access to secure messaging
    And the user has got messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view the RU Ref, Subject, From, To, Date and time for each message

  @sm111_s04
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
  Scenario: User is able to view all the following details
    Given the user has got '2' messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view all received messages in reverse chronological order/latest first

  @sm114_s01
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
  Scenario: User is able to distinguish unread messages in their inbox
    Given the user has no messages in their inbox
    When the user has an unread message in their inbox
    And they navigate to the inbox messages
    Then they are able to distinguish that the message is unread

  @sm114_s02
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
  Scenario: Messages are no longer distinguished as unread once they have been viewed
    Given the user has no messages in their inbox
    When the user has an unread message in their inbox
    And they navigate to the inbox messages
    And they view the unread message
    And they navigate to the inbox messages
    Then the message is no longer marked as unread

  @sm127_s02
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
  Scenario: User views 10 messages when 15 are there
    Given the user has no messages in their inbox
    And the user has got '15' messages in their inbox
    When they navigate to the inbox messages
    Then they are able to view '10' messages
    And the pagination links are available

  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
  Scenario: Internal User views new conversations
    Given both the internal and external users have started '3' conversations
    When they navigate to initial conversations
    Then they are able to view '3' messages