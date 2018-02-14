Feature: Display reporting unit page
  As an internal user
  I need to to be able to view reporting unit details
  So that I can undertake a number of potential actions related to that reporting unit

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us044_s01
  Scenario: The reporting unit details are presented to the user
    Given the reporting unit 49900000001 is in the system
    When the internal user views the 49900000001 reporting unit page
    Then the internal user is displayed the correct reporting unit details
