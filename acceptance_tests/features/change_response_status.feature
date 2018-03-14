Feature: Change response status
  As an internal user
  I need to change the case response status to completed by phone for an RU for a specific CE for a specific survey
  So that the respondent can complete the survey over the phone and they do not receive reminders

  @us050_s01
  Scenario: Internal user change response status
    Given the internal user is on the reporting unit page for 49900000003
    When the internal user changes the response status from 'Not started' to 'Completed by phone' for 49900000003
    And the internal user opens the Bricks data panel
    Then the status 'Completed by phone' is displayed back to the internal user

 @us050_s02
  Scenario: Respondent can view response status change
    Given the survey for 49900000002 has been completed by phone
    When the respondent goes to the history page
    Then the survey for 49900000002 has the status completed by phone
