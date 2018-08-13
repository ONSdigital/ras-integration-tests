@social
Feature: Search social cases by postcode
  As a Survey Enquiry Line User
  I need to be able find a case by entering a postcode
  So that I can find the right household related to the call

  Background: Internal user is already signed in and social survey exists
    Given the internal user is already signed in
    And a social survey exists

  @sus002-01
  Scenario: User needs to be able to search for a case by postcode
    Given the SEL user receives a phone call from a respondent
    When they enter a postcode
    Then all address are returned for the postcode

  @sus002-02
  Scenario: User needs to enter a full postcode when searching
    Given the SEL user receives a phone call from a respondent
    When they search for a partial postcode
    Then no postcodes/addresses are to be returned

  @sus002-03
  Scenario: The format of the postcode to be entered is XX11 X11 - supporting spaces and no spaces
    Given the format of the postcode entered is XX11 X11
    When the user clicks search
    Then all address are returned for the postcode

  @sus002-04
  Scenario: The format of the postcode to be entered is XX11X11 - supporting spaces and no spaces
    Given the format of the postcode entered is XX11X11
    When the user clicks search
    Then all address are returned for the postcode

  @sus002-05
  Scenario: User is to be informed if we do not hold the postcode that has been entered
    Given the user enters a postcode that doesnt exist in the sample
    When the internal user searches for that postcode
    Then no postcodes/addresses are to be returned