@business
@standalone
@fixture.setup.data.default
Feature: Site navigation
  As a Product Owner
  I need my users to easily navigate through the internal system
  So that they can get to the page they wish to view

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: User navigates to collection exercise
    Given a collection exercise has been created
    When the internal user navigates to the home page
    Then the user can view and click on a link to the surveys list page
    And the user can view and click on a link to the survey page
    And the user can view and click on a link to the collection exercise page
