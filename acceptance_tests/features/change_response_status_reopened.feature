Feature: Change response status to reopened
  As a internal user
  I need to change the response status for an RU for a specific CE for a specific survey to Re-opened
  So that the status reflects the action that I have taken internally and externally

  @us050c_s01
  Scenario: Internal user change response status
    Given the internal user is on the reporting unit page for 49900000004
    When the internal user changes the response status from 'Completed by phone' to 'Reopened'
    Then the status 'Reopened' is displayed back to the internal user

 @us050a_s02
  Scenario: Respondent can view response status change
    Given the survey for 49900000005 has been reopened
    When the respondent goes to the my surveys page
    Then the survey for 49900000005 has the status reopened
