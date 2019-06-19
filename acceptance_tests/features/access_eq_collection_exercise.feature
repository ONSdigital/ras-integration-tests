@standalone
@business
Feature: Respondent can access an eQ CE
  As a Respondent
  I need to be able to access an eQ CE
  So that I can see the CI for which I have been asked to submit data for on behalf of the specific RU

  Background: User already logged in
    Given the respondent is signed into their account


  # Should be a unit test, blows up on 'When' if using firefox.
  @skip
  @us062-accessEqCE_s01
  @fixture.setup.data.with.enrolled.respondent.user.and.eq.collection.exercise.live
  Scenario: Access eQ CE
    Given the respondent has a CE for an eQ available
    When the respondent accesses the eQ CE
    Then the respondent is redirected to eQ with a token
