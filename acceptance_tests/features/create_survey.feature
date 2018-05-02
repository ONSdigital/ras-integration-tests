Feature: As an internal user
  I need to be able to create new surveys
  So that new surveys can be handled by SDC

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us101-s01
  Scenario Outline: Internal user is able to create a new survey
    Given the internal user has entered the create survey URL
    When they enter the new survey details as reference <survey_id>, title <survey_title>, abbreviation <survey_abbreviation> and legal basis <survey_legal_basis>
    Then they can view the survey with reference <survey_id>, title <survey_title>, abbreviation <survey_abbreviation> and legal basis <survey_legal_basis>

    Examples: Test survey data
    | survey_id | survey_title                 | survey_abbreviation | survey_legal_basis           |
    | 9999      | Test Survey                  | CREATE              | Statistics of Trade Act 1947 |


