@business
@standalone
@fixture.setup.data.with.internal.user.and.collection.exercise.to.scheduled.status
Feature: View collection exercise details
  As a Collection Exercise Coordinator
  I need to view the details for a single collection exercise
  So that I am assured the collection exercise is correct

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: View collection exercise details
    Given a collection exercise exists
    When the internal user navigates to the collection exercise details page
    Then the user is able to view the survey details and period for that survey

  Scenario: View collection exercise events
    Given a collection exercise exists
    When the internal user navigates to the collection exercise details page
    Then the user is able to view the event dates for that collection exercise

  Scenario: View collection exercise variable events
    Given a collection exercise exists
    When the internal user navigates to the collection exercise details page
    Then the user is able to view the variable event dates for that collection exercise