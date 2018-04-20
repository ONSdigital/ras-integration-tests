Feature: Remove a loaded SEFT CI
  As a Collection Exercise Coordinator
  I need to be able to remove a  loaded SEFT CI
  So that the correct CI is associated to the RU

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us059-unselectCI_s01
  Scenario: The user is able to remove loaded SEFT CI
    Given I am on the collection exercise details screen with a loaded CI
    When I click the remove loaded SEFT CI button
    Then The loaded SEFT CI is removed

  @us059-unselectCI_s02
  Scenario: The user is not able to remove loaded SEFT CI when collection exercise state is 'Ready For Live'
    Given I am on the collection exercise details screen with a loaded CI
    When the collection exercise state is 'ready for live'
    Then I am not able to remove the loaded SEFT CI
