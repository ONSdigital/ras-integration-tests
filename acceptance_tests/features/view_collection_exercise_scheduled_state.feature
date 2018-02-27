Feature: View scheduled state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the 'Scheduled' state of a collection exercise 
  So that I know that the mandatory event dates exist for the collection exercise

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us041_s001
  Scenario: The 'Scheduled' state is displayed for a collection exercise that has event dates
    Given the mandatory event dates collection exercise for 1803 exist
    When the user navigates to the collection exercise details page for 1803
    Then the state of the collection exercise is Scheduled

  @us041_s002
  Scenario: The state can be viewed on the survey details page
    Given the user is on the Survey Page
    When they navigate to the Survey Details page
    Then they are able to see the Status for each collection exercise

  @us041_s003
  Scenario: The state can be viewed on the collection exercise details page
    Given the user is on the Survey Details Page
    When they navigate to the Collection Exercise Details Page
    Then they are able to see the Scheduled Status for that Collection Exercise
