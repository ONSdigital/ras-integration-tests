@business
@standalone

Feature: As an internal user
  I need to be able to change a respondents details
  So that the data held in the system is correct

  Background: Internal user is already signed in
    Given the internal user is already signed in

  @us057-s01
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: The internal user is able to change a respondents first name, last name and contact number
    Given the internal user has found the respondents details
    When they choose to change the name of a respondent
    Then the respondent account details become editable

  @us057-s02
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: All fields are required to be populated
    Given the internal user chooses to change account details
    When they remove the old contact number
    And they click save
    Then the changes will not be saved and they are informed that all fields are required

  @us057-s03
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: The internal user is able to save any changes made to the account details
    Given the internal user chooses to change account details
    When they change the contact number
    And they click save
    Then they are navigated back to the RU Details page
    And they are provided with confirmation the changes have been saved

  @us057-s04
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: The internal user is able to cancel out of changing the respondent details at any point
    Given the internal user chooses to change account details
    When they change the contact number
    And they decide to cancel
    Then they are navigated back to the RU Details page
    And the contact number is not changed

  @us058-s001
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: The user is able to edit the email address of a respondent
    Given the internal user has found the respondents details
    When they change the email address
    And they click save
    Then they are presented with confirmation that the changes have been saved
    And they can see the old and the unverified new email

  @us058-s002
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: The user is able to cancel out of changing the respondent details at any point
    Given the internal user chooses to change account details
    When they change the email address
    And they decide to cancel
    Then they are navigated back to the RU Details page
    And the email is not changed

  @us058-s003
  @fixture.setup.data.with.2.enrolled.respondent.users.and.internal.user
  Scenario: The user is to be informed if the email address entered is already in use and is unable to save
    Given the internal user chooses to change account details
    When they save an email address that is already in use
    Then they are informed that the email address they have entered is already in use


  @us216-s01
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: The user is able to click on the edit contact details link and be redirected to the form.
    Given the internal user has navigated to a respondents details page
    When they click on Edit Contact Details
    Then they are redirected to the Edit Contact Details form

  @us216-s02
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: When the user presses cancel on the edit contact details page they are returned to the respondents page.
    Given the internal user has navigated to a respondents details page
    When they click on Edit Contact Details
    And they decide to cancel
    Then they are redirected to the respondents page

  @us216-s03
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: When the user presses save changes without making changes they are redirected and informed no changes needed.
    Given the internal user has navigated to a respondents details page
    When they click on Edit Contact Details
    And they click save changes without making changes
    Then they are redirected to the respondents page and an info box is displayed stating no changes were made

  @us216-s02
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: When the user changes the name of the respondent they are redirected and informed via an info panel.
    Given the internal user has navigated to a respondents details page
    When they click on Edit Contact Details
    And they change the first and last name
    And they click save
    Then they are provided with confirmation the changes have been saved

  @us216-s02
  @fixture.setup.data.with.enrolled.respondent.user.and.internal.user
  Scenario: When the user changes the email of a respondent they are redirected and informed that a new verification email is sent
    Given the internal user has navigated to a respondents details page
    When they click on Edit Contact Details
    And they change the email address
    And they click save
    Then they are provided with confirmation that the email address has been changed
