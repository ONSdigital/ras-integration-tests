@business
@standalone
Feature: Add a survey
  As a Respondent
  I need to be able to enrol for a new survey with my existing account
  So that I can respond on behalf of a business

  Background: User already logged in
    Given the respondent is signed into their account

  @fixture.setup.data.with.enrolled.respondent.and.additional.iac
  Scenario: User is trying to add a survey using a new iac code that they have previously added
    Given the user has entered a valid enrolment code for a survey they have already added
    When they continue and confirm that the organisation and survey that they are enrolling for is correct
    Then the user is notified they have already added the survey
