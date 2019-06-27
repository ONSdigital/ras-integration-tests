Feature: Disable respondent enrolment status
  As an internal user
  I need to be able to disable the enrolment for a respondent
  So that the respondent can no longer access the survey

  Background: User already logged in
    Given the internal user is already signed in

  @us022_s01
  Scenario: Internal user must be able to disable a respondents enrolment
    Given the respondent with email "disable_respondent_1@email.com" is enrolled and active
    And the internal user is on the ru details page
    When the internal clicks on the disable button for "disable_respondent_1@email.com"
    And the internal user confirms they want to disable the account
    Then "disable_respondent_1@email.com"'s enrolment appears "Disabled" on the ru details page

  @us023_s01
  Scenario: Internal user must be able to re-enable a respondents enrolment
    Given the respondent with email "reenable_respondent_1@email.com" is enrolled and active
    And the internal user is on the ru details page
    When the internal clicks on the disable button for "reenable_respondent_1@email.com"
    And the internal user confirms they want to disable the account
    And the internal user is back on the ru details page
    When the internal clicks on the re-enable button for "reenable_respondent_1@email.com"
    And the internal user confirms they want to re-enable the account
    Then "reenable_respondent_1@email.com"'s enrolment appears "Enabled" on the ru details page

  @us022_s02
  Scenario: Internal user disables a respondents enrolment the respondent should no longer be able to view this enrolment
    Given the respondent with email "disable_respondent_2@email.com" is enrolled and active
      And the internal user is already signed in
      And the internal user disables enrolment for respondent with email "disable_respondent_2@email.com"
    When the respondent is signed into their account
      And the respondent with email "disable_respondent_2@email.com" views their survey todo list
    Then the respondent should not be able to view the disabled enrolment

  @us022_s03
  Scenario: Internal user disables a respondents enrolment the other respondent should still see survey
    Given the respondent with email "disable_respondent_3@email.com" is enrolled and active
      And the respondent with email "disable_respondent_4@email.com" is enrolled and active
      And the internal user is already signed in
      And the internal user disables enrolment for respondent with email "disable_respondent_3@email.com"
      And the internal user signs out
    When the respondent is signed into their account
      And the respondent with email "disable_respondent_4@email.com" views their survey todo list
    Then the respondent should see the survey in their todo list

  @standalone
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: internal user clicks link to change enrolment status on respondent page
    Given the internal user has navigated to a respondents details page
    When the user clicks either disable or re-enable
    Then the user is redirected to a confirmation screen

  @standalone
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
   Scenario: internal user clicks confirm button on confirmation screen
     Given the internal user has navigated to a respondents details page
     When the user clicks either disable or re-enable
     And the user clicks the confirm button
     Then the user is redirected to the respondents page and a success message is displayed
