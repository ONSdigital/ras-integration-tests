Feature: Disable respondent enrolment status
  As an internal user
  I need to be able to disable the enrolment for a respondent
  So that the respondent can no longer access the survey

  Background: User already logged in
    Given the internal user is already signed in

  @us022_s01
  Scenario: Internal user must be able to disable a respondents enrolment
    Given the respondent with email "disable_respondent_1@email.com" is enrolled and active
    And the internal user is on the ru details page
    When the internal clicks on the disable button for "disable_respondent_1@email.com"
    And the internal user confirms they want to disable the account
    Then "disable_respondent_1@email.com"'s enrolment appears "Disabled" on the ru details page
