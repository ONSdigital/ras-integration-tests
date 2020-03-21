@business
@standalone
@fixture.setup.data.with.internal.user.and.collection.exercise.to.created.status
Feature: As an internal user
  I need to be able to create a collection exercise
  So that I can add business events, collection instruments and sample

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us102-s01
  Scenario: Internal user is able to create a collection exercise
    Given internal user wants to create a collection exercise
    When they click create collection exercise
    And they complete the required fields and save
    When the collection exercise is created
    Then they are taken to the collection exercise list for that survey