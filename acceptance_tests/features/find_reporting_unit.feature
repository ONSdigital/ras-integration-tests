Feature: Find Reporting Unit
   As an internal user
   I need to be able to find a Reporting Unit
   So that I can easily locate the RU to deal with issues

  Background: Internal user is already signed in
    Given The internal user is already signed in

  Scenario: Find a Reporting Unit by its Reference Ref
    Given the internal user navigates to the find RU page
    When the internal user enters a RU Ref
    Then the Reporting Unit is displayed back to the user
    And the internal user signs out

  Scenario: Find a Reporting Unit by its Company Name
    Given the internal user navigates to the find RU page
    When the internal user enters a RU Name
    Then the Reporting Unit is displayed back to the user
    And the internal user signs out
