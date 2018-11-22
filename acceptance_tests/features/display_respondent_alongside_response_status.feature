@standalone
@wip
Feature: Internal user can search for a respondent via email
  As an internal user
  I need to be able to search for a registered respondent via their email
  So that I can easily find them when dealing with operational calls

#
#  Background: internal user is already signed in
#    Given the respondent is signed into their account

  @fixture.setup.data.enrolled.respondent
  @us211_01
  Scenario: Respondent field must be present on each Survey displayed on Reporting units for any given Reference
    Given an external user is enrolled onto a given survey
    And has not initiated any changes to the "Not started" status
    When an internal user navigates to Reporting units for that Reference
    Then no Respondent name should be displayed in the Respondent field
#
#  @fixture.setup.data.enrolled.respondent
#  Scenario: Respondent field must be updated once an external user has completed a survey online
#    Given an external user is enrolled onto a given survey
#    And the status is set to Completed
#    When an internal user navigates to Reporting Units for that reference
#    Then the Respondent details must be displayed in the Respondent field

