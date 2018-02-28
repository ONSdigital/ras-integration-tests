Feature: Change response status
  As an internal user
  I need to change the case response status to completed by phone for an RU for a specific CE for a specific survey
  So that the respondent can complete the survey over the phone and they do not receive reminders

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us050_s01
  Scenario: Change response status
    Given the reporting unit 49900000001 is in the system
    When the internal user views the 49900000001 reporting unit page
    And the internal user navigates to the change response status page for Bricks 201801
    And the internal user changes the response status from 'Not started' to 'Completed by phone'
    Then the status 'Completed by phone' is displayed back to the internal user

  # Test the external UI for completed by phone
