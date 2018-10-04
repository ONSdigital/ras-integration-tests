Feature: Internal User unlocking Respondent account
  As Internal User
  I need to be able to unlock a respondent's account
  So that the respondent can access their survey account

  Background: A respondent has locked their account
    Given A respondent with an email "locked@email.com" locks their account


  @us203_01
  Scenario: Internal user can view account is locked with an unlock link
    Given The internal user is already signed in
    And The internal user navigates to the find RU page
    When The internal user enters a RU ref
    Then The internal user can see that the respondent has an account status locked
    And There is also an unlock link below the locked

  @us203_02
  Scenario: Internal user clicks unlock
    Given An internal user clicks on the unlock link
    When They confirm the unlock
    Then The reporting unit page is reloaded with a change flag
    And Account status for the respondent is showing as active