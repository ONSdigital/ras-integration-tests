Feature: Set a collection exercise as ready for live
  As a Collection Exercise Coordinator
  I need to be able to set the collection exercise as 'Ready for Live'
  So that I know that all of the collection exercise details are correct and ready for the collection exercise to go live

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us028_s001
  @us028_s008
  Scenario: Once the user is happy with the contents of the collection exercise, they are able to set the collection exercise as 'Ready for Live'
    Given "rsi" "201912" is in the ready for review state
    And the user has checked the contents of "rsi" "201912" and it is all correct
    When they confirm that the collection exercise is ready to go live
    Then the user is informed that the collection exercise is setting as ready for live
    And when refreshing the page once processing has completed, the status is changed to Ready for Live

  @us028_s002
  Scenario: On choosing to set the collection exercise as 'Ready for Live', the user is asked to confirm before continuing and given the option to cancel
    Given "rsi" "201806" is in the ready for review state
    And the user has checked the contents of "rsi" "201806" and it is all correct
    When they choose to set the collection exercise as ready for live
    Then they are asked for confirmation before continuing

  @us028_s006
  Scenario: The user is to be informed if the system is processing the collection exercise
    Given "rsi" "201806" is in the ready for review state
    And the user has checked the contents of "rsi" "201806" and it is all correct
    When they confirm that the collection exercise is ready to go live
    Then they are to be informed that the system is setting the status as Ready for Live

  @us028_s007
  Scenario: The user is able to refresh the page at any point
    Given "rsi" "201805" is in the ready for review state
    And the user has confirmed that "rsi" "201805" is ready for go live
    When they navigate to "rsi" "201805" details screen
    And the system is setting the collection exercise as ready for live
    Then the user is able to refresh the page to see if there are any updates to the status

  @us028_s011
  Scenario: When the user sets the collection exercise as 'Ready for Live' no further changes can be made to the collection exercise
    Given "rsi" "201807" is in the ready for review state
    And the user has checked the contents of "rsi" "201807" and it is all correct
    When they confirm that the collection exercise is ready to go live
    Then they are no longer able to change the CIs, Sample or Mandatory Event Dates
