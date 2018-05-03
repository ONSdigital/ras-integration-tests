Feature: As an internal user
  I need to be able to change a respondents details
  So that the data held in the system is correct

  Background: Internal user is already signed in
    Given the internal user is already signed in
    And the respondent with email "test_respondent@test.com" is enrolled

  @us057-s01
  Scenario: The internal user is able to change a respondents first name, last name and contact number
    Given the internal user has found the "test_respondent@test.com" respondents details
    When they choose to change the name of a respondent
    Then the respondent account details become editable

  @us057-s02
  Scenario: All fields are required to be populated
    Given the internal user chooses to change "test_respondent@test.com" account details
    When they remove the old contact number
    And they click save
    Then the changes will not be saved and they are informed that all fields are required

  @us057-s03
  Scenario: The internal user is able to save any changes made to the account details
    Given the internal user chooses to change "test_respondent@test.com" account details
    When they change the contact number
    And they click save
    Then they are navigated back to the RU Details page
    And they are provided with confirmation the changes have been saved

  @us057-s04
  Scenario: The internal user is able to cancel out of changing the respondent details at any point
    Given the internal user chooses to change "test_respondent@test.com" account details
    When they change the contact number
    And they decide to cancel
    Then they are navigated back to the RU Details page
    And the contact number is not changed

  @us058-s001
  Scenario: The user is able to edit the email address of a respondent
    Given the respondent with email "test_respondent2@test.com" is enrolled
    And the internal user has found the "test_respondent2@test.com" respondents details
    When they change the email address to "new_respondent@test.com"
    And they click save
    Then they are presented with confirmation that the changes have been saved
    And they can see the old email address of "test_respondent2@test.com" and the unverified new email "new_respondent@test.com"

  @us058-s002
  Scenario: The user is able to cancel out of changing the respondent details at any point
    Given the internal user chooses to change "test_respondent@test.com" account details
    When they change the email address to "new_respondent@test.com"
    And they decide to cancel
    Then they are navigated back to the RU Details page
    And the email is not changed

  @us058-s003
  Scenario: The user is to be informed if the email address entered is already in use and is unable to save
    Given the internal user chooses to change "test_respondent@test.com" account details
    When they save an email address that is already in use
    Then they are informed that the email address they have entered is already in use
