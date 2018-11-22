@business
@standalone
@fixture.setup.data.with.internal.user
Feature: Display enrolment code
  As an internal user
  I need to display unused code for a RU for a specific survey
  So that the code can be provided to a respondent/RU over the phone

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: Display an unused active code
    Given the internal user views the reporting unit page for a sample unit
    When the internal user opens the survey data panel
    Then an unused enrolment code is displayed back to the user
