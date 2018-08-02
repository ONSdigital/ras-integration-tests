Feature: As an internal user
  I need to enrol in a survey

  Background: Internal user has received an enrolment code
    Given the internal user has received an enrolment code

  # todo WIP - Wording subject to BA approval

  @ade  #todo remove?
  Scenario: Internal user enrols in a survey
    When the internal user views the survey enrolment page
    And enters an enrolment code
    Then confirms the correct survey is selected
    And completes the account details page
    Then the internal user can see they have successfully enrolled in a survey
