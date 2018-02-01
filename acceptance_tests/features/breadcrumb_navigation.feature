Feature: Breadcrumb Navigation
  As an internal user
  I need to understand where I am within the system's hierarchical structure
  So that I can navigate back through the hierarchy

  Background: Internal user is already signed in
    Given The internal user is already signed in

  Scenario: User navigates to the surveys page from collection exercise
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page for QBS 1803
    And the user clicks the survey breadcrumb link
    Then the user is taken to the surveys page
    And the internal user signs out

  Scenario: User navigates to the homepage
    Given the user accesses the system
    When the internal user navigates to the home page
    Then the user does not see a breadcrumbs trail
    And the internal user signs out

  Scenario: User can tell which page they are on in the hierarchical structure
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page for QBS 1803
    Then the user can see breadcrumbs showing the site hierarchy
    And the internal user signs out
