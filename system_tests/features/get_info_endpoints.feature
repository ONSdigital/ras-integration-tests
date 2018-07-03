Feature: Get info endpoints

  Scenario Outline: System hits service get info endpoint
    Given services are running
    When  the system requests <service> endpoint info
    Then  a success status code (200) is returned

   Examples: Services
    |service |
    |action  |
    |action exporter |
    |case |
    |collection exercise |
    |collection instrument |
    |django |
    |frontstage |
    |iac |
    |notify gateway |
    |party |
    |response operations ui |
    |respondent home ui |
    |sample |
    |secure message |
    |survey |
