Feature: Change response status
  As an internal user
  I need to change the case response status to completed by phone for an RU for a specific CE for a specific survey
  So that the respondent can complete the survey over the phone and they do not receive reminders

  Background: Internal user is already signed in and a respondent is enrolled on a new collection exercise
    Given the internal user is already signed in
    And the "Bricks" "204901" collection exercise has been executed
    And the respondent has been enrolled for "Bricks" "204901" for ru "49900000001"

  @us050_s01
  Scenario: Internal user can change the response status to Completed by phone
    Given the internal user is on the reporting unit page for ru ref "49900000001"
    And the "Bricks" "204901" collection exercise for ru "49900000001" is in the "Not started" status
    When the internal user changes the response status for "Bricks" "204901" to "Completed by phone"
    Then the "Bricks" "204901" collection exercise for ru "49900000001" is in the "Completed by phone" status

  @us050_s02
  Scenario: Internal user can change the response status to No Longer Required
    Given the internal user is on the reporting unit page for ru ref "49900000002"
    And the "Bricks" "204901" collection exercise for ru "49900000002" is in the "Not started" status
    When the internal user changes the response status for "Bricks" "204901" to "No longer required"
    Then the "Bricks" "204901" collection exercise for ru "49900000002" is in the "No longer required" status

  @us050_s03
  Scenario: Respondent can view response status change
    Given the respondent has been enrolled for Bricks 204901 for ru 49900000001 which is in Completed by phone status
    When the respondent goes to the history page
    Then the respondent is presented the "bricks" "204901" "49900000001" status as "Completed by phone"