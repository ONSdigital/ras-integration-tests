Feature: Internal user can search for a respondent via email
  As an internal user
  I need to be able to search for a registered respondent via their email
  So that I can easily find them when dealing with operational calls


  @us091_s01
  Scenario: Search verified respondent by email address
    Given the respondent account with email example@example.com has been created
    And the respondent email is verified
    When an internal user searches for respondent using their email address
    Then the respondent details should be displayed

  @us091_s02
  Scenario: Search non-existent respondent by email address
    Given the respondent account with email test@test.com has not been created
    When the internal user searches for the respondent using the email test@test.com
    Then the internal user is given a message of no respondent for email
