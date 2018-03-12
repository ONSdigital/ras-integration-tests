Feature: Disable respondent enrolment status
  As an internal user
  I need to be able to disable the enrolment for a respondent
  So that the respondent can no longer access the survey

  @us022_s01
  Scenario: Internal user must be able to disable a respondents enrolment
    Given the internal user is on the ru details page
    When the internal user requests the respondent enrolment to be disabled
    Then the respondent's enrolment appears disabled on the ru details page for enrolment

  @us022_s02
  Scenario: Internal user has to confirm when choosing to disable respondent enrolment
    Given the internal user is on the ru details page
    When the internal user requests the respondent enrolment to be disabled
    Then the internal user has to confirm they want to disable respondent's enrolment

  @us022_s03
  Scenario: Internal user disables a respondents enrolment the repondent should no longer be able to view this enrolment
    Given the internal user disables a respondents enrolment
    When the respondent views their survey todo list
    Then the respondent should not be able to view the disabled enrolment