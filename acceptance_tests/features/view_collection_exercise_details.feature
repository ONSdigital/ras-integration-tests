Feature: View collection exercise details
  As a Collection Exercise Coordinator
  I need to view the details for a single collection exercise
  So that I am assured the collection exercise is correct

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: View collection exercise details
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page for QBS 1803
    Then the user is able to view the survey details and period for that survey
    And the internal user signs out

  Scenario: View collection exercise events
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page for QBS 1803
    Then the user is able to view the event dates for that collection exercise
    And the internal user signs out
