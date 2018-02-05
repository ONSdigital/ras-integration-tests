Feature: Display RU details
  As an internal user
  I need to be able to view RU details
  So that I can undertake a number of potential actions related to that RU

  Background: Internal user is already signed in
    Given The internal user is already signed in

  @us044-displayRU_s01
  Scenario: The RU details are presented
    Given The internal user has accessed the page reporting unit page
    When The RU Details are displayed back to the user
    Then The user should see the RU Ref
    And the internal user signs out