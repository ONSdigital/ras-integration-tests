@standalone
@business
@fixture.setup.data.with.enrolled.respondent.user.and.internal.user
Feature: Internal User unlocking Respondent account
  As Internal User
  I need to be able to unlock a respondent's account
  So that the respondent can access their survey account

  Background: A respondent has locked their account
    Given a respondent locks their account
    And the internal user is already signed in

  @us203_01
  Scenario: Internal user can view account is locked with an unlock link
    When the internal user navigates to locked accounts RU page
    Then the internal user can see that the respondent has an account status locked
    And there is also an unlock link below the locked

  @us203_02
  Scenario: Internal user clicks unlock
    Given the internal user navigates to locked accounts RU page
    When an internal user clicks on the unlock link
    And they confirm the unlock
    Then the reporting unit page is reloaded with a change flag
    And account status for the respondent is showing as active