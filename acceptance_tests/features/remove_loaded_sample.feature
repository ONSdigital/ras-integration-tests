@standalone
@business
Feature: Remove loaded sample
  As a collection Exercise Coordinator
  I need to be able to remove a loaded sample
  So that I can replace it with the correct sample

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us053-s01
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.scheduled.status
  Scenario: Remove a loaded sample
    Given user on the collection exercise details screen
    When they click on remove loaded sample
    And confirm they want to proceed with the action
    Then the loaded sample is removed

  @us053-s02
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.scheduled.status
  Scenario: Display successful sample removed message
    Given user has proceeded to remove loaded sample
    When they click on remove loaded sample
    And the loaded sample has been removed
    Then they are presented with a successful sample removal message
    And check sample content is displayed instead of remove loaded sample
    And the collection exercise status will reflect the sample has been removed

  @us053-s03
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.ready.for.live.status
  Scenario: Don't Display remove loaded sample from Ready For Live state
    Given user wants to remove a loaded sample from a collection exercise
    When the collection exercise has status is ready for live
    Then remove loaded sample must not be displayed