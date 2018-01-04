Feature: View collection exercise
  As a Collection Exercise Coordinator
  I need to view the details for a single collection exercise
  So that I am assured the collection exercise are correct

  Scenario: View attributes for a single collection exercise
    Given the 2017 collection exercise for the BRES survey exists
    When the internal user views the 2017 collection exercise for the BRES survey
    Then the internal user can view the collection exercise details
