Feature: As an internal user
  I need to be able to edit/amend survey details
  So that I can change/update survey details when required

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us106-s01
  Scenario: Internal user is able to edit/amend survey details
    Given the internal user is on the survey list page
    When they request to edit/amend a surveys details
    And they edit/amend the survey details
    Then they can view the updated survey details
      | survey_id | survey_title                 | survey_abbreviation | survey_legal_basis   |
      | 199       | National Balance Sheet 2.0   | NBS_2.0             | Voluntary Not Stated |
    And they request to reset survey details
    Then the data is reset
