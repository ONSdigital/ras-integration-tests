Feature: Notification letter
   As a Business Survey Coordinator
   I need letters to be sent to reporting units
   So that reporting units can enrol in surveys

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: Notification file
    Given a reporting unit has been enrolled in a survey
    When the survey goes live
    Then the reporting unit will receive a letter