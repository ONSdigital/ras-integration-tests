Feature: As an internal user
  I need to be able to change a respondents details
  So that the data held in the system is correct


  Scenario: The internal user is able to change a respondents first name, last name and contact number
    Given: the internal user has found the respondents details
    When: they choose to change the name of a respondent
    Then: the respondent account details become editable

  Scenario: The internal user is able to enter up to 254 characters for the first and last name
    Given: the internal user chooses to change the name of a respondent
    When: they change the first and last name
    Then: they are able to enter up to 254 characters

  # TODO: Check if this scenario is required
  Scenario: The internal user must enter a valid contact number
    Given: the internal user chooses to change the contact number of a respondent
    When: they change the contact number
    Then: the number entered must be a valid phone number

  Scenario: The internal user is able to save any changes made to the account details
    Given: the internal user chooses to change the account details
    When: they change the contact number and save the changes
    And: confirm they are correct
    Then: they are provided with confirmation that the contact number has been changed

  Scenario: The internal user is presented with the details that should be updated for confirmation
    Given: the internal user had updated the contact number
    When: they choose to update details, they are presented with the contact number that has been changed
    Then: they are able to confirm the changes

  Scenario: The internal user is to receive on-screen confirmation that the system has saved the changes
    Given: the changes made are correct
    When: they confirm the changes
    Then: they are presented with confirmation that the changes have been saved and what has been changed