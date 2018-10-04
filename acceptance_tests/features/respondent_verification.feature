Feature: notifying respondent to verify their email address
  As an external user
  I need to be notified that I haven't verified my email
  So that I can verify my email address

  Background: A respondent has to have created an account
    Given The respondent has created an account which is unverified called "unverified2@email.com"

  Scenario: Unverified account user is notified to verify their email address
    Given An external "unverified2@email.com" with unverified account tried to sign into their account
    When They enter correct credentials
    Then They are shown on-screen notification to verify their email
    And They are shown on-screen notification to request a verification link email

  Scenario: Respondent using expired verification link
    Given A user has an expired verification link
    When They click the expired verification link
    Then The user is notified that their link has expired, and given the option to re-send a verification email

  Scenario: User has the ability to re-send their verification email
    Given A user has been notified their link has expired
    When They select the re-send verification email link
    Then They are notified that their verification email has been re-sent

  Scenario: Verifying a users account
    Given A user has received a verification link
    When They select the verification link in the email "unverified2@email.com"
    Then The user is taken to a page stating their account has been activated

