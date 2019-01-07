@business
@standalone
@fixture.setup.data.with.internal.user.and.collection.exercise.to.scheduled.status
Feature: View ready for review state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the 'Ready for Review' state of a collection exercise
  So that I know that all of the mandatory components of a collection exercise have been populated

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us042_s01
  Scenario: The 'Ready for Review' state is displayed after a collection instrument is loaded
    Given the collection exercise is Scheduled
    And the user has loaded the sample
    When the user loads the collection instruments
    Then the collection exercise is Ready for Review

  @us042_s02
  Scenario: The 'Ready for Review' state is displayed after a sample is loaded
    Given the collection exercise is Scheduled
    And the user has loaded the collection instruments
    When the user loads the sample
    Then the collection exercise is Ready for Review

  @us042_s03
  Scenario: The 'Ready for Review' state of a collection exercise is displayed in survey details
    Given the collection exercise has a loaded sample and collection instruments
    When the user navigates to the survey details page
    Then the collection exercise is Ready for Review
