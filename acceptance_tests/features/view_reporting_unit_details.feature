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
    Then the internal user is presented with the associated collection exercises

  @us046_s01
  Scenario: Able to view respondent details for the RU Ref for the survey
    Given the reporting unit 49900000001 is in the system
    When the internal user views the 49900000001 reporting unit page
    Then the internal user is presented with the associated respondents
