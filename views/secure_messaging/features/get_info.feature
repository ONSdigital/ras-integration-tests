Feature: Get info

  Scenario: User hits get info endpoint
    Given the user requests endpoint info
    Then  the endpoint info is returned
    And   a success status code (200) is returned