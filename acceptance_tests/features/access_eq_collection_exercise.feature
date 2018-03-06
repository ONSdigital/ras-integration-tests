Feature: Respondent can access an eQ CE
  As a Respondent
  I need to be able to access an eQ CE
  So that I can see the CI for which I have been asked to submit data for on behalf of the specific RU

  Background: User already logged in
    Given the respondent is signed into their account

  @us062-accessEqCE_s01
  Scenario: Access eQ CE
    Given the respondent has a CE for an eQ available
    When the respondent accesses the eQ CE
    Then the respondent lands on the correct eQ Homepage for the survey and CE and CI
