Feature: Disable respondent enrolment status
  As an internal user
  I need to be able to disable the enrolment for a respondent
  So that the respondent can no longer access the survey

  @us022_s01
  Scenario: Internal user must be able to disable a respondents enrolment
    Given the respondent with email "disable_respondent_1@email.com" is enrolled
    And the internal user is on the ru details page
    When the internal clicks on the disable button for "disable_respondent_1@email.com"
    And the internal user confirms they want to disable the account
    Then "disable_respondent_1@email.com"'s enrolment appears disabled on the ru details page

#  @us022_s02
#  Scenario: Internal user disables a respondents enrolment the repondent should no longer be able to view this enrolment
#    Given the internal user disables a respondents enrolment
#    When the respondent views their survey todo list
#    Then the respondent should not be able to view the disabled enrolment