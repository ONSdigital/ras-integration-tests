Feature: Search social cases by postcode
  As a Survey Enquiry Line User
  I need to be able find a case by entering a postcode
  So that I can find the right household related to the call

  Background: Internal user is already signed in
    Given the internal user is already signed in
    Given a social survey case exists

  @sus002-01
  Scenario: User needs to be able to search for a case by postcode
    Given The SEL user receives a phone call from a respondent
    When They enter a postcode
    Then All address are returned for the postcode

  @sus002-02
  Scenario: User needs to enter a full postcode when searching
    Given The SEL user receives a phone call from a respondent
    When They search for a partial postcode
    Then No postcodes/addresses are to be returned

  @sus002-03
  Scenario: The format of the postcode to be entered is XX11 X11 - supporting spaces and no spaces
    Given The format of the postcode entered is XX11 X11
    When The user clicks search
    Then All address are returned for the postcode

  @sus002-04
  Scenario: User is to be informed if we do not hold the postcode that has been entered
    Given The user enters a postcode that doesnt exist in the sample
    When The internal user searches for that postcode
    Then No postcodes/addresses are to be returned