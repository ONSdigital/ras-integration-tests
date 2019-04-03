@standalone
Feature: internal users can re-send the verification email
  as an internal user
  I need to be able to re-send respondents verification emails
  so that when something goes wrong they can recover their account

  @fixture.setup.data.with.internal.user.and.unverified.respondent
  Scenario: an internal user clicks confirm on the resend verification email confirmation page
    Given the internal user is already signed in
    And the internal user has navigated to a respondents details page
    And the internal user clicks re-send verification email
    When they press confirm
    Then they are redirected to the respondents page and a confirmation message is displayed

  @fixture.setup.data.with.internal.user.and.unverified.respondent
  Scenario: an internal user clicks cancel on the resend verification email confirmation page
    Given the internal user is already signed in
    And the internal user has navigated to a respondents details page
    And the internal user clicks re-send verification email
    When they press cancel
    Then they are redirected to the respondents page