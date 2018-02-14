Feature: View ready for review state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the 'Ready for Review' state of a collection exercise
  So that I know that all of the mandatory components of a collection exercise have been populated

  Background: Internal user is already signed in
    Given: the internal user is already signed in

  @us042_s01
  Scenario: The 'Ready for Review' state is to be displayed when a sample and collection instrument are loaded
    Given the 201803 collection exercise for the QIFDI survey has been created
    When the internal user navigates to the collection exercise details page for QIFDI 201803
    And the status of the collection exercise is Scheduled
    And the user loads the sample
    And the user loads the collection instruments
    Then the status of the collection exercise is Ready for Review
    And the internal user signs out
