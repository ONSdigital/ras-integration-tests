@business
@standalone
@fixture.setup.data.with.internal.user.and.collection.exercise.to.created.status
Feature: View the state of a collection exercise on the details page
  As a Collection Exercise Coordinator
  I need to be able to view the state of a collection exercise 
  So that I can manage the collection exercise as required

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: View the state of a single collection exercise
    Given a collection exercise exists
    When the internal user navigates to the collection exercise details page
    Then the user is able to view the status of the collection exercise
