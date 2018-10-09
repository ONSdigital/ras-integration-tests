@standalone
Feature: Breadcrumb Navigation
  As an internal user
  I need to understand where I am within the system's hierarchical structure
  So that I can navigate back through the hierarchy

  Background: Internal user is already signed in
    Given the internal user is already signed in

  Scenario: User navigates to the surveys page from collection exercise
    Given a collection exercise has been created
    When the internal user navigates to the collection exercise details page
    And the user clicks the survey breadcrumb link
    Then the user is taken to the surveys page

  @default_data_setup_not_required
  Scenario: User navigates to the homepage
    Given the user accesses the system
    When the internal user navigates to the home page
    Then the user does not see a breadcrumbs trail

  Scenario: User can tell which page they are on in the hierarchical structure
    Given a collection exercise has been created
    When the internal user navigates to the collection exercise details page
    Then the user can see breadcrumbs showing the site hierarchy
