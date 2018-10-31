@standalone
Feature: Change response status
  As an internal user
  I need to change the case response status to completed by phone for an RU for a specific CE for a specific survey
  So that the respondent can complete the survey over the phone and they do not receive reminders

  Background: Internal user is already signed in and a respondent is enrolled on a new collection exercise
    Given the internal user is already signed in

  @us050_s01
  @fixture.setup.data.enrolled.respondent
  Scenario: Internal user can change the response status to Completed by phone
    Given the internal user is on the reporting unit page
    And the collection exercise is in the "Not started" status
    When the internal user changes the response status to "Completed by phone"
    Then the collection exercise is in the "Completed by phone" status

  @us050_s02
  @fixture.setup.data.enrolled.respondent
  Scenario: Internal user can change the response status to No Longer Required
    Given the internal user is on the reporting unit page
    And the collection exercise is in the "Not started" status
    When the internal user changes the response status to "No longer required"
    Then the collection exercise is in the "No longer required" status

  @us050_s03
  @fixture.setup.data.enrolled.respondent.generate.new.iac.collection.exercise.live
  Scenario: Respondent can view response status change
    Given the respondent has had their response status changed to Completed by phone
    When the respondent goes to the history page
    Then the respondent is presented the status as "Completed by phone"