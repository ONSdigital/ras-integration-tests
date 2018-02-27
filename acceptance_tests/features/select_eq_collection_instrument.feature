Feature: Select eQ Collection Instruments
  As a Collection Exercise Coordinator
  I need to be able to select the eQ collection instruments in the system for a given collection exercise
  and given survey
  So that the collection instrument can be associated with the RU's in the sample within the CE

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us029-selectEqCI_s01
  Scenario: The user is able to select the eQ collection instruments to load into the collection exercise
    Given the internal user navigates to the collection exercise details page for QBS 1803
    When the user selects the collection instrument
    Then the collection instrument is added into the collection exercise
