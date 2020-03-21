@standalone
@business
@fixture.setup.data.with.internal.user.and.collection.exercise.to.created.status

Feature: Create mandatory collection exercise event dates
  As an Collection Exercise Coordinator (Internal User)
  I need to be able to input mandatory business events dates per collection exercise
  So that a collection exercise can be processed and set to live

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: Collection Exercise co-ordinator attempts to enter invalid date
    Given the internal user enters an "mps" event date for the survey
    When the user enters a date of "50" "January" "2040"
    And they submit the event date
    Then an error message should appear identifying invalid date entered
    And mps date should not appear on collection exercise details page
