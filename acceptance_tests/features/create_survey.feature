Feature: As an internal user
  I need to be able to create new surveys
  So that new surveys can be handled by SDC

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us101-s01
  Scenario: Internal user is able to create a new survey
    Given the internal user has entered the create survey URL
    When they enter the new survey details
    Then they can view the newly created survey details
      | survey_id | survey_title                 | survey_abbreviation | survey_legal_basis           |
      | 9999      | Test Survey                  | CREATE              | Statistics of Trade Act 1947 |
