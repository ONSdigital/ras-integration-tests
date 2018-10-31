@business
@standalone
@fixture.setup.data.default
Feature: As an respondent user
  I need to enrol in a survey

  Background: Respondent user has received an enrolment code
    Given the respondent is ready to enrol in a survey

  Scenario: Frontstage can see the survey they are enrolling in
    Given a respondent has got their enrolment code
    When they enter their enrolment code
    Then they confirm the survey and organisation details

  Scenario: Frontstage user can create an account
    Given a respondent has entered their enrolment code
    And they confirm the survey and organisation details
    When they enter their account details
    Then they are sent a verification email
