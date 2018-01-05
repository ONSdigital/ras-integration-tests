Feature: View collection exercise
  As a Collection Exercise Coordinator
  I need to view the details for a single collection exercise
  So that I am assured the collection exercise are correct

  Scenario: View collection exercise details
    Given the 2017 collection exercise for the BRES survey has been created
    When the internal user navigates to the collection exercise details page
    Then the user is able to view the survey details and period for that survey
