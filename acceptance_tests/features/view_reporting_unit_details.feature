Feature: View reporting unit details
  As an internal user
  I need to be able to view the surveys, CEs and respondents associated to the RU Ref
  So that I can understand for any RU Ref, the surveys and CEs they are selected for
  and I understand the relationships with respondents for the Reporting Unit across surveys

  Scenario: Able to view all surveys associated to the displayed RU Ref
    Given the reporting unit 49900000005 is in the system
    When the internal user views the 49900000005 reporting unit page
    Then the internal user is presented with the associated surveys
    And the surveys are sorted by Survey Code

  Scenario: Able to view all collection exercises associated to the displayed RU Ref
    Given the reporting unit 49900000005 is in the system
    When the internal user views the 49900000005 reporting unit page
    Then the internal user is presented with the associated collection exercises
      | period |      reporting_unit_name       | region |    status   |
      | 201801 | OFFICE FOR NATIONAL STATISTICS | GB     | Not started |
    And the collection exercises are sorted by Go Live date
