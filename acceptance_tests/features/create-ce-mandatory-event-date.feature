Feature: Create mandatory collection exercise event dates
  As an Collection Exercise Coordinator (Internal User)
  I need to be able to input mandatory business events dates per collection exercise
  So that a collection exercise can be processed and set to live

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us103_s01
  Scenario: Collection Exercise co-ordinator should be able to enter mandatory event dates per CE
    Given the internal user has created a new collection exercise for "MBS" and period "205001" with shown as "January 2050"
    When there is no mandatory event dates scheduled for the ce for "205001"
    Then The user must be able to input the mandatory event dates into the CE for a given survey

  @us103_s02
  Scenario: Collection Exercise co-ordinator attempts to enter invalid date
    Given the internal user has chosen to enter a mandatory ce event date
    When the user enters an invalid date
    And submits mandatory ce event date
    Then an error message should appear identifying invalid date entered
    And invalid date should not appear on ce details page

  @us103_s03
  Scenario: Collection Exercise co-ordinator enters mandatory event date redirected to ce details page
    Given the internal user has chosen to enter a mandatory ce event date
    When the user enters a valid date
    And submits mandatory ce event date
    Then the user is redirected to the ce details page
    And the new mandatory event date is displayed
