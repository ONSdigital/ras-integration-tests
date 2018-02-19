Feature: View scheduled state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the 'Scheduled' state of a collection exercise 
  So that I know that the mandatory event dates exist for the collection exercise

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us041_s01
  Scenario: The 'Scheduled' state is displayed for a collection exercise that has event dates
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the survey details page for QBS
    Then the status of the collection exercise is listed as Scheduled

  @us041_s02
  Scenario: The 'Scheduled' state is displayed on the details page for a collection exercise that has event dates
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page for QBS 1803
    Then the status of the collection exercise is displayed as Scheduled

  @us041_s03
  Scenario: The 'Scheduled' state is displayed after events are loaded
    Given the 201806 collection exercise for the Bricks survey is Created
    When the user loads the mandatory events
    Then the status of the collection exercise is displayed as Scheduled
