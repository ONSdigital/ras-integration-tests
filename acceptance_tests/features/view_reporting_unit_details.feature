Feature: View reporting unit details
  As an internal user
  I need to be able to view the surveys, CEs and respondents associated to the RU Ref
  So that I can understand for any RU Ref, the surveys and CEs they are selected for
  and I understand the relationships with respondents for the Reporting Unit across surveys

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us044_s01
  Scenario: The reporting unit details are presented to the user
    Given the reporting unit 49900000001 is in the system
    When the internal user views the 49900000001 reporting unit page
    Then the internal user is displayed the correct reporting unit details

  @us045_s01
  Scenario: Able to view all surveys associated to the displayed RU Ref
    Given the reporting unit 49900000001 is in the system
    When the internal user views the 49900000001 reporting unit page
    Then the internal user is presented with the associated surveys

  @us045_s02
  Scenario: Able to view all collection exercises associated to the displayed RU Ref
    Given the reporting unit 49900000001 is in the system
    When the internal user views the 49900000001 reporting unit page
    And the internal user opens the Bricks data panel
    Then the internal user is presented with the associated collection exercises

  @us046_s01
  Scenario: Able to view respondent details for the RU Ref for the survey
    Given the reporting unit 49900000001 is in the system
    And the respondent "first_name" is enrolled
    When the internal user views the 49900000001 reporting unit page
    And the internal user opens the Bricks data panel
    Then the internal user is presented with the associated respondents

  @us047_s01
  Scenario: "Trading as" name is displayed on Reporting Units page
    Given the reporting unit 49900000007 is in the system
    When the internal user views the 49900000007 reporting unit page
    Then the "trading as" name should be displayed on the RU details

  @us047_s01
  Scenario: If no "Trading As" name, no further information should be provided
    Given the reporting unit 49900000008 is in the system
    When the internal user views the 49900000008 reporting unit page
    Then the "trading as" name should not appear on the RU details

