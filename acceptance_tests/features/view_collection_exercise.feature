Feature: View Collection Exercise
  As a Collection Exercise Coordinator
  I need to view all collection exercises for a specific survey
  So that I can manage the collection exercises

  Scenario: View all collection exercises for an annual survey
    Given collection exercises for "BRES" exist in the system
    When the internal user views the collection exercise page for "BRES"
    Then the internal user can view relevant attributes for the survey
      | survey_id | survey_title                            | survey_abbreviation | survey_legal_basis           |
      | 221       | Business Register and Employment Survey | BRES                | Statistics of Trade Act 1947 |
    And the internal user can view all collection exercises for "BRES"


#  Scenario: View all collection exercises for a quarterly survey
#    Given collection exercises for "QBS" exist in the system
#    When the internal user views the collection exercise page for "QBS"
#    Then the internal user can view relevant survey attributes for "QBS"
#      | survey_id | survey_title              | survey_abbreviation | survey_legal_basis           |
#      | 139       | Quarterly Business Survey | QBS                 | Statistics of Trade Act 1947 |
#    And the internal user can view all collection exercises for "QBS"
#
#
#  Scenario: View all collection exercises for a monthly survey
#    Given collection exercises for "MWSS" exist in the system
#    When the internal user views the collection exercise page for "MWSS"
#    Then the internal user can view relevant survey attributes for "MWSS"
#      | survey_id | survey_title                      | survey_abbreviation | survey_legal_basis           |
#      | 134       | Monthly Wages and Salaries Survey | MWSS                | Statistics of Trade Act 1947 |
#    And the internal user can view all collection exercises for "MWSS"


#  Scenario: No collection exercises exist
#    Given no collection exercises for a survey exist in the system
#    When the internal user views the page
#    Then the internal user views an empty table