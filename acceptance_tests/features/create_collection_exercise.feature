Feature: As an internal user
  I need to be able to create a collection exercise
  So that I can add business events, collection instruments and sample

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us102-s01
  Scenario: Internal user is able to create a collection exercise
    Given internal user wants to create a collection exercise
    When they click create collection exercise
    And they complete the required fields and save
    When the collection exercise is created
    Then they are taken to the collection exercise list for that survey

  @us102-s02
  Scenario: Each collection exercise must be uniquely identified within the system
    Given internal user is creating a collection exercise
    Then they click create collection exercise
    When they enter period details that is in use by an existing collection exercise
    Then they are presented with an error screen
    And they are asked to use different details

  @us102-s03
  Scenario: Each collection exercise period field must have a maximum of 6 digit character
    Given internal user is creating a collection exercise
    Then they click create collection exercise
    When they enter details into the period field
    Then they can only enter a maximum of six characters

  @us102-s04
  Scenario: Each collection exercise must be associated to a specific survey
    Given internal user is creating a CE for a specific survey
    Then they click create collection exercise
    When they have created the CE
    Then the CE must be associated to the specific survey
