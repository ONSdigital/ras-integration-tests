@business
@standalone
Feature: Add a survey
  As a Respondent
  I need to be able to enrol for a new survey with my existing account
  So that I can respond on behalf of a business

  Background: User already logged in
    Given the respondent is signed into their account

  @skip
  @fixture.setup.data.with.enrolled.respondent.and.additional.iac
  Scenario: User is trying to add a survey using a new iac code that they have previously added
    Given the user has entered a valid enrolment code for a survey they have already added
    When they continue and confirm that the organisation and survey that they are enrolling for is correct
    Then the user is notified they have already added the survey

  @fixture.setup.data.with.unenrolled.respondent.user
  @us334-addSurvey_s01
  Scenario: Select to add new survey
    When access to do list in my surveys
    Then they are able to add a new survey

  @fixture.setup.data.with.unenrolled.respondent.user
  @us334-addSurvey_s02
  Scenario: Enter the enrolment code
    When they add a new survey
    Then they are able to enter an enrolment code

  @fixture.setup.data.with.unenrolled.respondent.user.and.new.iac
  @us334-addSurvey_s03
  Scenario: View survey & organisation that they are enrolling for
    Given selects to add a new survey
    When they enter a valid enrolment code
    Then they are to be presented with the survey and organisation that they are enrolling for

  @fixture.setup.data.with.unenrolled.respondent.user
  @us334-addSurvey_s04
  Scenario: Invalid entry of an enrolment code
    Given selects to add a new survey
    When they enter an invalid enrolment code
    Then they are to be notified

  @fixture.setup.data.with.unenrolled.respondent.user.and.new.iac.and.collection.exercise.to.live
  @us334-addSurvey_s05, @enrolment, @smoke
  Scenario: View new survey in my surveys
    Given the user has entered a valid enrolment code
    When they continue and confirm that the organisation and survey that they are enrolling for is correct
    Then the new survey is to be listed in My Surveys and confirmation is presented to the user

  @fixture.setup.data.with.unenrolled.respondent.user
  @us334-addSurvey_s06
  Scenario: User can cancel at any point
    Given the user has entered a valid enrolment code
    When they navigate to the confirm organisation page and click cancel
    Then the user is navigated back to their "To do" list and they have not enrolled for that survey


