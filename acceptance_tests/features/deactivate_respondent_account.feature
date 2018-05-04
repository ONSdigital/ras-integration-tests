Feature: Internal user can deactivate a respondent's account
  As an internal user
  I need to be able to deactivate a respondent's account
  So that the systems have the correct respondent

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us020_s01
  Scenario: All enrolments displayed to internal user before deactivating an account
    Given the internal user is on the reporting unit details page
    And the respondent with email "deactivate_account@gmail.com" is enrolled and active
    When the internal user selects to deactivate respondent's "deactivate_account@gmail.com" account
    Then all the respondent's enabled enrolments should be displayed

  @us020_s02
  Scenario: Ability to suspend account
    Given the internal user is on the reporting unit details page
    And the respondent with email "deactivate_account@gmail.com" is enrolled and active
    And the internal user has selected to deactivate a respondent "deactivate_account@gmail.com" account
    When the internal user confirms suspension of account
    Then the respondent "deactivate_account@gmail.com" account is suspended
    And confirmation of suspended account presented to user

  @us020_s03
  Scenario: Respondent with suspended account cannot access system
    Given respondent with email "deactivate_account@gmail.com" has a suspended account
    When the suspended respondent attempts to sign in with email "deactivate_account@gmail.com"
    Then presented with notification of wrong login details
