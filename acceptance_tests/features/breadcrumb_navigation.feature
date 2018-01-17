Feature: Breadcrumb Navigation
  As an internal user
  I need to understand where I am within the system's hierarchical structure
  So that I can navigate back through the hierarchy

  Scenario: User navigates to the homepage
    Given the 1803 collection exercise for the QBS survey has been created
    When the internal user navigates to the collection exercise details page
    And the user clicks the survey breadcrumb link
    Then the user is taken to the surveys page

