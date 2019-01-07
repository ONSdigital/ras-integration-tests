@business
@standalone
@fixture.setup.data.with.internal.user.and.collection.exercise.to.created.status
Feature: View sample
   As a Collection Exercise Coordinator
   I need to understand the content of a sample
   So that I am reasonably assured that it is the right sample file for the collection exercise

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: View sample in context of the specific collection exercise
    Given the user has loaded the sample in context of a collection exercise
    When the internal user navigates to the collection exercise details page
    Then the user is able to view the sample loaded for that collection exercise