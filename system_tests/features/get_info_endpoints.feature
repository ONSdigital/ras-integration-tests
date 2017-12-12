Feature: Get info endpoints

  Scenario Outline: System hits service get info endpoint
    Given the system requests <service> endpoint info
    When  the <service> endpoint info is returned
    Then   a success status code (200) is returned

   Examples: Services
    |service |
    |action  |
    |action exporter |
    |backstage |
    |backstage ui |
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
