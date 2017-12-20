Feature: View Collection Exercise

  Scenario: View all collection exercises
    Given collection exercises for a survey exist in the system
    When the internal user views the collection exercise page
    Then the internal user can view relevant attributes for a survey
      | attribute   |
      | Long name   |
      | Short name  |
      | Legal basis |
      | Survey ID   |
#    And the internal user can view all collection exercises for a survey
#      |


#  Scenario: No collection exercises exist
#    Given no collection exercises for a survey exist in the system
#    When the internal user views the page
#    Then the internal user views an empty table