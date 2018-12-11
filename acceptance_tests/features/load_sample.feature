@business
@standalone
@fixture.setup.data.with.internal.user.and.collection.exercise.to.scheduled.status
Feature: Load sample
   As a Collection Exercise Coordinator
   I need to be able to load the sample
   So that a sample file exists in the system

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: Preview sample
    Given the internal user navigates to the collection exercise details page
    When the user selects a sample
    Then the user is presented with sample details

  Scenario: Cancel preview sample
    Given the user is presented with sample details
    When the user cancels the sample
    Then the sample details are reset

  Scenario: Load sample
    Given the collection exercise has been created
    When the internal user navigates to the collection exercise details page
    Then the user is able to load the sample
