Feature: Load ASHE sample
   As a Collection Exercise Coordinator
   I need to be able to load an ASHE sample
   So that a sample file exists in the system

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us081_s001
  Scenario: Load ASHE sample
    Given the 201803 collection exercise for the ASHE survey has been created
    When the internal user navigates to the collection exercise details page for ASHE 201803
    Then the user is able to load the ASHE sample file