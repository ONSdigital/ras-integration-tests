Feature: As an internal user
  I need to be able to change a respondents details
  So that the data held in the system is correct

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @skip
  @us057-s01
  Scenario: The internal user is able to change a respondents first name, last name and contact number
    Given the internal user has found the respondents details for 49900000001
    When they choose to change the name of a respondent
    Then the respondent account details become editable

  @skip
  @us057-s02
  Scenario: The internal user is able to enter up to 254 characters for the first and last name
    Given the internal user chooses to change the account details
    When they change the first and last name
    And they click save
    Then they are able to enter up to 254 characters

  @skip
  @us057-s03
  Scenario: All fields are required to be populated
    Given the internal user chooses to change the account details
    When they remove the old contact number
    And they click save
    Then the changes will not be saved and they are informed that all fields are required

  @skip
  @us057-s04
  Scenario: The internal user is able to save any changes made to the account details
    Given the internal user chooses to change the account details
    When they change the contact number
    And they click save
    Then they are navigated back to the RU Details page
    And they are provided with confirmation the changes have been saved

  @skip
  @us057-s05
  Scenario: The internal user is able to cancel out of changing the respondent details at any point
    Given the internal user chooses to change the account details
    When they change the contact number
    And they decide to cancel
    Then they are navigated back to the RU Details page
    And the contact number is not changed