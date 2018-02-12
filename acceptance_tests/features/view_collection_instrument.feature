Feature: View Collection Instruments
  As a Collection Exercise Coordinator
  I need to view the collection instruments that the system holds for the given collection exercise
  So that I am assured that the right CI is available for the right RU(s)

    Background: Internal user is already signed in
      Given the internal user is already signed in

    Scenario: View Collection Instruments
      Given the collection instruments have been loaded
      When the user navigates to the collection exercise details page
      Then they are able to see the filename of all collection instruments that have been loaded
      And the internal user signs out
