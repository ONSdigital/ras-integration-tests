Feature: Preview sample
  As a Collection Exercise Coordinator
  I need to be able to check the sample details before loading into the system
  So I am reassured that the right sample is presented for loading

  Scenario: Preview sample
    Given the internal user navigated to the collection exercise details page
    When the user selects a sample
    Then the user is presented with sample details

  Scenario: Cancel preview sample
    Given the user is presented with sample details
    When the user cancels the sample
    Then the sample details are reset