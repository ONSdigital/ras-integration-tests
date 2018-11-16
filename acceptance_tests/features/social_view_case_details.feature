@social
@standalone
@fixture.setup.data.with.internal.user
Feature: View social case details
  As a Survey Enquiry Line User
  I need to be able to view the case details in relation to the call I have received
  So that I can confirm the household details and take any further action

  Background: Internal user is already signed in and social survey exists
  Given the internal user is already signed in to social UI
  And a social survey exists

  @sus003-01
  Scenario: Users are able to view their case details
    Given SEL searches for a postcode
    When they select the address
    Then they can see all the above case details