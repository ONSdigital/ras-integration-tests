@standalone
@business
@fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live
Feature: Internal user can search for a respondent via email
  As an internal user
  I need to be able to search for a registered respondent via their email
  So that I can easily find them when dealing with operational calls


  @us211_01
  Scenario: Respondent field must be present on each Survey displayed on Reporting units for any given Reference
    Given an external user is enrolled onto a given survey
    And has not initiated any changes to the "Not started" status
    When an internal user navigates to Reporting units for that Reference
    Then no Respondent name should be displayed in the Respondent field

  @skip
  Scenario: Respondent field must be updated once an external user has completed a survey online
    Given  a user has completed a survey online
    And the status is set to Completed
    When an internal user navigates to Reporting Units for that reference
    Then the Respondent details must be displayed in the Respondent field

  Scenario: Respondent field must not be updated once an external user has partially completed a survey online
    Given a user has partially completed a survey (In progress)
    And  the status is set to In Progress
    When an internal user navigates to Reporting Units for that reference
    Then no Respondent name should be displayed in the Respondent field

  Scenario: Respondent field must not be updated once an external user has completed a survey via phone
    Given a user has completed a survey via the telephone
    And the status is set to "Completed by phone"
    When an internal user navigates to Reporting Units for that reference
    Then no Respondent name should be displayed in the Respondent field

  Scenario: Respondent field must not be updated once an external user is no longer required to complete a survey
    Given an internal user has set a given survey to "No longer required" for a given respondent
    And the status is set to "No longer required"
    When an internal user navigates to Reporting Units for the no longer required reference
    Then no longer required should be displayed in the survey collection exercise