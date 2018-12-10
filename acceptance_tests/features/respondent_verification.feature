@standalone
@business
@fixture.setup.data.with.unverified.respondent
Feature: notifying respondent to verify their email address
  As an external user
  I need to be notified that I haven't verified my email
  So that I can verify my email address

  Scenario: Unverified account user is notified to verify their email address
    Given the respondent with unverified account navigates to the sign in page
    When they enter correct credentials
    Then they are shown on-screen notification to verify their email
    And they are shown on-screen notification to request a verification link email

  Scenario: Respondent using expired verification link
    When the respondent clicks an expired verification link
    Then the user is notified that their link has expired, and given the option to re-send a verification email

  Scenario: User has the ability to re-send their verification email
    Given the respondent has clicked an expired account verification link
    And the user has been notified their link has expired
    When they select the re-send verification email link
    Then they are notified that their verification email has been re-sent

  Scenario: Verifying a users account
    When the respondent clicks a valid verification link in the email
    Then the user is taken to a page stating their account has been activated
