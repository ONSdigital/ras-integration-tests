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

  Scenario: The user does not enter a reminder , should not see option to add reminders 2 or 3
    Given the internal user adds an "mps" event date of "15" "July" "2040" for the survey
    And the internal user adds an "go_live" event date of "16" "July" "2040" for the survey
    When the internal user adds an "return_by" event date of "17" "July" "2040" for the survey
    Then the add reminder "2" option should not be displayed
    And the add reminder "3" option should not be displayed

  Scenario: The user does enters a reminder , should see option to add reminders 2 but not 3
    Given the internal user adds an "mps" event date of "15" "July" "2040" for the survey
    And the internal user adds an "go_live" event date of "16" "July" "2040" for the survey
    And the internal user adds an "return_by" event date of "17" "July" "2040" for the survey
    When the internal user adds an "reminder" event date of "18" "July" "2040" for the survey
    Then the add reminder "2" option should be displayed
    And the add reminder "3" option should not be displayed

  Scenario: The user does enters reminder and reminders 2 and 3 all dates should be visible on details
    Given the internal user adds an "mps" event date of "15" "July" "2040" for the survey
    And the internal user adds an "go_live" event date of "16" "July" "2040" for the survey
    And the internal user adds an "return_by" event date of "17" "July" "2040" for the survey
    And the internal user adds an "reminder" event date of "18" "July" "2040" for the survey
    And the internal user adds an "reminder2" event date of "19" "July" "2040" for the survey
    When the internal user adds an "reminder3" event date of "20" "July" "2040" for the survey
    Then the new "mps" date of "15" "July" "2040" is displayed
    And the new "go_live" date of "16" "July" "2040" is displayed
    And the new "return_by" date of "17" "July" "2040" is displayed
    And the new "reminder" date of "18" "July" "2040" is displayed
    And the new "reminder2" date of "19" "July" "2040" is displayed
    And the new "reminder3" date of "20" "July" "2040" is displayed
