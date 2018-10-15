@business
@standalone
@fixture.setup.data.unenrolled.respondent.generate.new.iac
Feature: Generate new enrolment code
  As an internal user
  I need to obtain a new enrolment code for a RU for a specific survey
  So that the code can be provided to a respondent/RU over the phone

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us051-generateNewCode_s01
  Scenario: Make a request for a new code
    Given the internal user views the reporting unit page for a sample unit
    When the internal user opens the survey data panel
    And the user clicks generate enrolment code
    Then a new enrolment code is displayed back to the user
