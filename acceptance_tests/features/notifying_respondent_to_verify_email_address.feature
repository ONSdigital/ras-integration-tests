Feature: notifying respondent to verify their email address
  As an external user
  I need to be notified that I haven't verified my email
  So that I can verify my email address

  Background: A respondent has to have created an account
    Given the respondent has created an account which is unverified


  @us205_01
  Scenario: Unverified account user is notified to verify their email address
    Given an external user with unverified account tried to sign into their account
    When they enter correct credentials
    Then they are shown on-screen notification to check their email

  @us206_01
  Scenario: User is notified that their link has expired
    Given a user is notified their link has expired
    When they select the verification link in the email
    Then the user is taken to a page stating their account has been activated

#  @us206_01
#  Scenario: User is notified that their link has expired
#    Given a user has received a verification email
#    When they select the verification link in the email
#    And it's been more than 80 hours since the email was sent
#    Then the user is notified that their link has expired, and given the option to re-send a verification email
#
#  @us206_02
#  Scenario: User has the ability to re-send their verification email
#    Given a user has been notified their link has expired
#    When they select the re-send verification email link
#    Then they are notified that their verification email has been re-sent