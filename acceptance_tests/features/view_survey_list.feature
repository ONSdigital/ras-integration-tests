Feature: View survey list
  As a Respondent
  I need to see collection exercise(s) only if the the event 'Go-Live' has occurred/passed
  So that collection exercises are not visible to respondents before they should be

  Background: User already logged in
    Given the respondent is signed into their account

  @us060-filterCEByGoLive_s01
  Scenario: Respondent can view collection exercise after the Go Live Event
    Given the go live event for the collection exercise has passed
    When the respondent views the survey list todo page
    Then the respondent is displayed that collection exercise

  @us060-filterCEByGoLive_s02
  Scenario: Respondent cannot view the collection exercise prior to the collection exercise Go Live Event
    Given the go live event for the collection exercise has not passed
    When the respondent views the survey list todo page
    Then the respondent is not displayed that collection exercise
