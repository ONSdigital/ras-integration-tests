Feature: Internal user can search for a respondent via email
  As an internal user
  I need to be able to search for a registered respondent via their email
  So that I can easily find them when dealing with operational calls

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us091_s01
  Scenario: Search verified respondent by email address
    Given the respondent account with email "example@example.com" has been created
    When an internal user searches for respondent using their email address "example@example.com"
    Then the respondent details should be displayed, email "example@example.com"

  @us091_s02
  Scenario: Search non-existent respondent by email address
    Given the respondent account with email "test@test.com" has not been created
    When the internal user searches for the respondent using the email "test@test.com"
    Then the internal user is given a message of no respondent for email
