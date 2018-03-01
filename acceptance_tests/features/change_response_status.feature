Feature: Change response status
  As an internal user
  I need to change the case response status to completed by phone for an RU for a specific CE for a specific survey
  So that the respondent can complete the survey over the phone and they do not receive reminders

  @us050_s01
  Scenario: Internal user change response status
    Given the reporting unit 49900000002 is in the system
    And the internal user is already signed in
    When the internal user views the 49900000002 reporting unit page
    And the internal user navigates to the change response status page for Bricks 201801
    And the internal user changes the response status from 'Not started' to 'Completed by phone'
    Then the status 'Completed by phone' is displayed back to the internal user

  @us050_s02
  Scenario: Respondent can view response status change
    Given the respondent is signed into their account
    And the survey for 49900000002 has been completed by phone
    When the respondent goes to the history page
    Then the survey for 49900000002 has the status completed by phone
