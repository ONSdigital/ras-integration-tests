Feature: Set a collection exercise as ready for live
  As a Collection Exercise Coordinator
  I need to be able to set the collection exercise as 'Ready for Live'
  So that I know that all of the collection exercise details are correct and ready for the collection exercise to go live


  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: Once the user is happy with the contents of the collection exercise, they are able to set the collection exercise as 'Ready for Live'
    Given the user has checked the contents of the collection exercise and it is all correct
    When they confirm set the collection exercise as ready to go live
    Then the collection exercise state is changed to Ready for Live
