@business
@standalone
Feature: View live state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the state of a collection exercise when it is Live
  So that I know which collection exercises have gone live

  Background: Internal user is already signed in
    Given the internal user is already signed in
    And a new collection exercise has been created

  @us047_s001
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.ready.for.live.status
  Scenario: The 'Live' state is to be displayed when the collection exercise goes live (the 'go live' date hits) and collection instrument is available to respondent
    Given the user has confirmed that the collection exercise is Ready for Live
    When the collection exercise go live date hits
    Then the state of a collection exercise is to be changed to Live

  @us047_s002
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.live.status
  Scenario: The state can be viewed on the survey details page
    Given the user is on the Survey Page
    When they navigate to the collection exercise page
    Then they are able to see the Live Status

  @us047_s003
  @fixture.setup.data.with.internal.user.and.collection.exercise.to.live.status
  Scenario: The state can be viewed on the collection exercise details page
    Given the user is on the collection exercise Page
    When they navigate to the Collection Exercise Details Page
    Then they are able to see the Live Status for that Collection Exercise
