Feature: View Collection Exercise
  As a Collection Exercise Coordinator
  I need to view all collection exercises for a specific survey
  So that I can manage the collection exercises


  Scenario: View attributes for a survey
    Given collection exercises for BRES exist in the system
    When the internal user views the collection exercise page for BRES
    Then the internal user can view relevant attributes for the survey
      | survey_id | survey_title                            | survey_abbreviation | survey_legal_basis           |
      | 221       | Business Register and Employment Survey | BRES                | Statistics of Trade Act 1947 |
    And the internal user can view all collection exercises for the survey
