Feature: As an internal user
  I need to be able to change a respondents details
  So that the data held in the system is correct

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us057-s01
  Scenario: The internal user is able to change a respondents first name, last name and contact number
    Given the internal user has found the respondents details
    When they choose to change the name of a respondent
    Then the respondent account details become editable

  @us057-s02
  Scenario: The internal user is able to enter up to 254 characters for the first and last name
    Given the internal user chooses to change the account details
    When they change the first and last name
    Then they are able to enter up to 254 characters

  @us057-s03
  Scenario: All fields are required to be populated
    Given the internal user chooses to change the contact number of a respondent
    When they remove the old contact number and click save
    Then the changes will not be saved and they are informed that all fields are required

  @us057-s04
  Scenario: The internal user is able to save any changes made to the account details
    Given the internal user chooses to change the account details
    When they change the contact number and save the changes
    Then they are navigated back to the RU Details page
    And they are provided with confirmation the changes have been saved

  @us057-s05
  Scenario: If an error occurs when saving, the user is to be informed and asked to try again
    Given the internal user changes the account details
    When they click save and the details are unable to be saved
    Then they are informed that an error occurred and to try again

  @us057-s06
  Scenario: The internal user is able to cancel out of changing the respondent details at any point
    Given the internal user chooses to change the account details
    When they decide to cancel
    Then they are navigated back to the RU Details page and no changes are saved