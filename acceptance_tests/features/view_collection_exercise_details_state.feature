Feature: View the state of a collection exercise on the details page
  As a Collection Exercise Coordinator
  I need to be able to view the state of a collection exercise 
  So that I can manage the collection exercise as required

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: View the state of a single collection exercise
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page for QBS 1803
    Then the user is able to view the status of the collection exercise
