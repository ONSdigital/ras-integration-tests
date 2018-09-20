@social
Feature: Change Response Status to 'Partial interview achieved but respondent requested data be deleted'
  As a: Survey Enquiry Line User
  I need: To be able to disable all UACs for a case when the response status is changed to 'Partial interview achieved but respondent requested data be deleted'
  So that: A respondent cannot enter their UAC and access the data they have previously entered

  Background: Social survey exists
    Given a social survey exists

  @sus006-01
  Scenario: The user is able to change the status of a case
    Given the SEL user has entered a status of '562 Partial interview achieved but respondent requested data be deleted'
    When the respondent enters a UAC
    Then they are informed that they are unable to launch the survey
