Feature: View response status
  As an internal user
  I need to view the case response status for an RU for a specific CE for a specific survey when completed
  So that I can view the date and timestamp of the completed state

  Background: Internal user is already signed in and a respondent is enrolled on a new collection exercise
    Given the internal user is already signed in

  @us208
  Scenario: Internal user can see the view link for response status Completed by phone
    Given the internal user is on the reporting unit page for ru ref "49900000001"
    And the "Bricks" "202001" collection exercise for ru "49900000001" is in the "Not started" status
    When the internal user changes the response status for "Bricks" "202001" to "Completed by phone"
    Then the "Bricks" "202001" collection exercise for ru "49900000001" displays a view link

  @us208
  Scenario: Internal user can view the date and timestamp for a completed survey in the response status panel
    Given the internal user is on the reporting unit page for ru ref "49900000001"
    And the "Bricks" "202001" collection exercise for ru "49900000001" is in the "Completed by phone" status
    When the internal user click view the response status for the survey with correct period
    Then the internal user can view the timestamp for the completed state
    And the only action available is the close link
