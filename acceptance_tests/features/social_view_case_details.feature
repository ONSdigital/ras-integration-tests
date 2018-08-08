Feature: View social case details
  As a Survey Enquiry Line User
  I need to be able to view the case details in relation to the call I have received
  So that I can confirm the household details and take any further action

  Background: Internal user is already signed in
  Given the internal user is already signed in
    And a social survey case exists

  @sus003-01
  Scenario: Users are able to view their case details
    Given: SEL searches for a postcode
    When: They select the address
    Then: They can see all the above case details