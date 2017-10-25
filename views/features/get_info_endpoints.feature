Feature: Get info endpoints

  Scenario Outline: User hits service get info endpoint
    Given the user requests <service> endpoint info
    When  the <service> endpoint info is returned
    Then   a success status code (200) is returned

   Examples: Services
    |service |
    |secure message |
    |frontstage |
    |backstage |
    |party |
    |collection instrument |
    |django |
    |api gateway |
