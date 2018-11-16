@social
@standalone
@fixture.setup.data.with.internal.user
Feature: Change Response Status
  As a: Survey Enquiry Line User
  I need: To be able to change the response status to an outcome that requires no further action
  So that: This is recorded on the system and no further actions are taken for these cases

  Background: Internal user is already signed in and social survey exists
    Given the internal user is already signed in to social UI
    And a social survey exists

  @sus005-01
  Scenario: The user is able to change the status of a case
    Given the SEL user has received a call and found the case details
    When they change the response status
    Then the new status is to be saved against that case

  @sus005-02
  Scenario: The user is able to select a status from the list below
    Given the SEL user has selected to change the status
    When the status is updated to '412 Legitimacy concerns'
    Then any further communication from being triggered such as pre-notification/invitation/reminder is prevented

  @sus005-03
  Scenario: The new status is to be reflected on the case details page
    Given the SEL user has selected a new response status
    When they confirm the status change
    Then the new response status is to be displayed on the case details page
