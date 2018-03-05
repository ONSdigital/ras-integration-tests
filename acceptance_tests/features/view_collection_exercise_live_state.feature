Feature: View live state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the state of a collection exercise when it is Live
  So that I know which collection exercises have gone live

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us047_s001
  Scenario: The 'Live' state is to be displayed when the collection exercise goes live (the 'go live' date hits) and collection instrument is available to respondent
    Given the user has confirmed that "bricks" "201801" is Ready for Live
    When "bricks" "201801" go live date hits
    Then the state of a collection exercise is to be changed to Live

  @us047_s002
  Scenario: The state can be viewed on the survey details page
    Given the user is on the Survey Page
    When they navigate to the "bricks" page
    Then they are able to see the Status for "201801"

  @us047_s003
  Scenario: The state can be viewed on the collection exercise details page
    Given the user is on the "bricks" Page
    When they navigate to the Collection Exercise Details Page for "201801"
    Then they are able to see the Live Status for that Collection Exercise
