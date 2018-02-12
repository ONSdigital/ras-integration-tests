Feature: Find Reporting Unit
   As an internal user
   I need to be able to find a RU
   So that I can easily locate the RU to deal with issues

  Background: Internal user is already signed in
    Given The internal user is already signed in

  Scenario: Find a RU by its Reference
    Given the internal user navigates to the find RU page
    When the internal user enters a RU ref
    Then the RU is displayed back to the user
    And the internal user signs out

  Scenario: Find a RU by its Company Name
    Given the internal user navigates to the find RU page
    When the internal user enters a RU name
    Then the RU is displayed back to the user
    And the internal user signs out

  Scenario: No RU found with search query
    Given the internal user navigates to the find RU page
    When the internal user enters a RU name that does not exist
    Then no results found is displayed back to the user
    And the internal user signs out