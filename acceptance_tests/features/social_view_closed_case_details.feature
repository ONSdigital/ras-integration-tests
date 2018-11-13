@social
@standalone
@fixture.setup.data.collection.exercise.closed.social
Feature: HAC cannot be generated if the collection exercise has closed
  As a Survey Enquiry Line User
  I need to ensure that a new code cannot be generated if the collection exercise has closed
  So that respondents do not attempt to access a closed collection exercise erroneously

  Background: Internal user is already signed in and social survey exists
  Given the internal user is already signed in to social UI
  And a social survey exists

  @ssus055-01
  Scenario: Users are able to view their case details
    Given SEL searches for a postcode
    When they select the address
    Then they can see all the above case details
    And they can see that the collection exercise is closed