Feature: Get info endpoints

  Scenario Outline: System hits service get info endpoint
    Given services are running
    When  the system requests <service> endpoint info
    Then   a success status code (200) is returned

   Examples: Services
    |service |
    |action  |
    |action exporter |
    |backstage |
    |case |
    |collection exercise |
    |collection instrument |
    |django |
    |frontstage-api |
    |frontstage |
    |iac |
    |notify gateway |
    |party |
    |response operations ui |
    |sample |
    |secure message |
    |survey |
