Feature: As an internal user
  I need to be able to edit/amend collection exercise details
  So that I can change/update collection exercise details when required

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us107-s01
  Scenario: Internal user is able to edit/amend collection exercise
    Given the internal user is on the collection exercise details page
    When they request to edit/amend collection exercise details
    And they edit/amend the details
    Then they can view the updated details
      | period | shown_to_respondent_as | status  |
      | 201906   | 12 June 2019         | Scheduled |

  @us107-s02
  Scenario: Internal user cannot edit/amend collection exercise period
    Given the internal user is on the collection exercise details page for RSI 201812
    When the state is at/after Ready for live
    Then they cannot edit the collection exercise period
