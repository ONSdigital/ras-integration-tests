@business
@standalone
@fixture.setup.survey.metadata.with.internal.user
Feature: As an internal user
  I need to be able to create new surveys
  So that new surveys can be handled by SDC

  Background: Internal user is already signed in
  Given the internal user is already signed in

  @us101-s01
  Scenario: Internal user is able to create a new survey
    Given the internal user has entered the create survey URL
    When they enter new survey details with legal basis of 'Statistics of Trade Act 1947'
    Then they are taken to survey list page
     And the new survey information is on the page
