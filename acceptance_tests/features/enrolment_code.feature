Feature: Generate new enrolment code
  As an internal user
  I need to obtain a new enrolment/display unused code for a RU for a specific survey
  So that the code can be provided to a respondent/RU over the phone

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us051-generateNewCode_s01
  Scenario: Make a request for a new code
    Given the internal user views the 49900000001 reporting unit page
    When the internal user opens the Bricks data panel
    And the user clicks generate enrolment code
    Then a new enrolment code is displayed back to the user

  Scenario: Display an unused active code
    Given the internal user views the 49900000001 reporting unit page
    When the internal user opens the Bricks data panel
    Then an unused enrolment code is displayed back to the user
