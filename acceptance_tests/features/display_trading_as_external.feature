Feature: Display "trading as" in To do and History
  As an external user
  I need to be able to see the "trading as" name for each survey in my to do and history list
  So that I know which company i need to collate data for and the one I have done

  Background: External user is logged in
    Given the respondent is signed into their account

  @us110-displayTradingAsExternal_s01
  Scenario: "Trading As" name is displayed for each survey in "to do" page
    Given a company has a separate trading name (s01)
    When the respondent views a survey in To do
    Then the "trading as" name should be displayed below the business name for every survey

  @us110-displayTradingAsExternal_s02
  Scenario: "Trading As" name is displayed for each survey in "history" page
    Given a company has a separate trading name (s02)
    When the respondent has completed a survey which is now in their history
    Then the trading name should be displayed below the business name for every survey

  @us110-displayTradingAsExternal_s03
  Scenario: If no "Trading As" name, no further information should be provided
    Given a company does not have a separate "trading as" name
    When the respondent views a survey in To do
    Then the "trading as" field should not appear on the RU details page