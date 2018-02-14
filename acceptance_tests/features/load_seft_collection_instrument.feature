Feature: Load SEFT collection instruments
  As a Collection Exercise Coordinator
  I need to be able to load the SEFT collection instruments in the system for a given collection exercise
    and given survey
  So that I am assured that the right collection instrument is available for the right RU


  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: Load collection instrument
    Given the 201803 collection exercise for the QIFDI survey has been created
    When the internal user navigates to the collection exercise details page for QIFDI 201803
    Then the user is able to load the collection instruments

  Scenario: Load collection instrument wrong file type selected
    Given the 201803 collection exercise for the QIFDI survey has been created
    When the internal user navigates to the collection exercise details page for QIFDI 201803
    And the internal user selects a non xlsx file
    Then an error message is displayed to the user

  Scenario: Load collection instrument wrong file type uploaded
    Given the 201803 collection exercise for the QIFDI survey has been created
    When the internal user navigates to the collection exercise details page for QIFDI 201803
    And the internal user loads a non xlsx file
    Then an error message is displayed to the user at the top of the screen

