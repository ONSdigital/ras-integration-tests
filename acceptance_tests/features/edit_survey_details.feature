@business
@standalone
Feature: As an internal user
  I need to be able to edit/amend survey details
  So that I can change/update survey details when required

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @fixture.setup.data.survey.with.internal.user
  @us106-s01
  Scenario: Internal user is able to edit/amend survey details
    Given the internal user is on the survey list page
    When they request to edit/amend a specific surveys details
      And they edit/amend the survey details
    Then the survey details match the updated values

