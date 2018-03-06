Feature: View Collection Exercise
  As a Collection Exercise Coordinator
  I need to view all collection exercises for a specific survey
  So that I can manage the collection exercises

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: View attributes for a survey
    Given collection exercises for QBS exist in the system
    When the internal user views the collection exercise page for QBS
    Then the internal user can view relevant attributes for QBS
      | survey_id | survey_title              | survey_abbreviation | survey_legal_basis           |
      | 139       | Quarterly Business Survey | QBS                 | Statistics of Trade Act 1947 |
    And the internal user can view all collection exercises for QBS
      | period | shown_to_respondent_as | status  |
      | 1803   | 9 March 2018           | Scheduled |
      | 1806   | 15 June 2018           | Scheduled |
      | 1809   | 14 September 2018      | Ready for live |
      | 1812   | 14 December 2018       | Scheduled |


  Scenario Outline: Ensure collection exercise exists for a survey
    Given all surveys have collection exercises
    When the internal user views the collection exercise page for <survey_abbreviation>
    Then there is at least one collection exercise

    Examples:
      | survey_abbreviation |
      | RSI                 |
      | AIFDI               |
      | AOFDI               |
      | QIFDI               |
      | QOFDI               |
      | Sand&Gravel         |
      | Blocks              |
      | Bricks              |
      | MWSS                |
      | PCS                 |
      | QBS                 |
      | ASHE                |
      | NBS                 |
      | OFATS               |
      | GovERD              |
      | BRES                |
