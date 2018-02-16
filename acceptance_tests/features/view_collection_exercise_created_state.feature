Feature: View created state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the state of a collection exercise when it is 'Created'
  So that I know that the collection exercise exists for a survey

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us040_s01
  Scenario: The 'Created' state is to be displayed when the collection exercise is created
    Given the collection exercises for that survey exist
    When the internal user navigates to the survey details page
    Then the status of a collection exercise is Created

  @us040_s02
  Scenario: The 'Created' state can be viewed on the collection exercise details page
    Given the internal user is on the survey details page
    When the internal user navigates to the collection exercise details page
    Then the displayed status should be Created
