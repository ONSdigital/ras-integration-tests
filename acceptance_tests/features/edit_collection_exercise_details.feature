@business
@standalone
Feature: As an internal user
  I need to be able to edit/amend collection exercise details
  So that I can change/update collection exercise details when required

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @fixture.setup.data.with.internal.user.and.collection.exercise.to.created.status
  @us107-s01
  Scenario: Internal user is able to edit/amend collection exercise
    Given the internal user navigates to the collection exercise details page
    When they request to edit/amend collection exercise details
    And they edit the collection exercise details
    Then the collection exercise details match the updated values


  @us107-s02
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.live.status
  Scenario: Internal user cannot edit/amend collection exercise period
    Given the internal user navigates to the collection exercise details page
    When the state is at/after Ready for live
    Then they cannot edit the collection exercise period
