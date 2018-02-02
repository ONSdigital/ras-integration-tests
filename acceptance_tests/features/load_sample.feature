Feature: Load sample
   As a Collection Exercise Coordinator
   I need to be able to load the sample
   So that a sample file exists in the system

  Background: Internal user is already signed in
    Given The internal user is already signed in

  Scenario: Preview sample
    Given the internal user navigates to the collection exercise details page for QBS 1803
    When the user selects a sample
    Then the user is presented with sample details
    And the internal user signs out

  Scenario: Cancel preview sample
    Given the user is presented with sample details for QBS 1803
    When the user cancels the sample
    Then the sample details are reset
    And the internal user signs out

  Scenario: Load sample
    Given the 201803 collection exercise for the QIFDI survey has been created
    When the internal user navigates to the collection exercise details page for QIFDI 201803
    Then the user is able to load the sample
    And the internal user signs out
