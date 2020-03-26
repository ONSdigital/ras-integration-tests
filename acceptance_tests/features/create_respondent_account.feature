@standalone
@business
@fixture.setup.data.with.respondent.user.data.and.new.iac
Feature: Registering a new respondent account
    As an external user
    I need to be able to register an account
    So that I can access the system and complete surveys

    Scenario: Frontstage user can create an account
        Given the respondent is ready to enrol in a survey
        And a respondent has entered their enrolment code
        And they confirm the survey and organisation details
        When they enter their account details
        Then they are sent a verification email