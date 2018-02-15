Feature: View ready for review state of a collection exercise
  As a Collection Exercise Coordinator
  I need to be able to view the 'Ready for Review' state of a collection exercise
  So that I know that all of the mandatory components of a collection exercise have been populated

  Background: Internal user is already signed in
    Given: the internal user is already signed in

  @us042_s01
  Scenario: The 'Ready for Review' state is displayed after a collection instrument is loaded
    Given the 201803 collection exercise for the QIFDI survey is Scheduled
    And the user has loaded the sample
    When the user loads the collection instruments
    Then the status of the collection exercise is Ready for Review

  @us042_s02
  Scenario: The 'Ready for Review' state is displayed after a sample is loaded
    Given the 201803 collection exercise for the QIFDI survey is Scheduled
    And the user has loaded the collection instruments
    When the user loads the sample
    Then the status of the collection exercise is Ready for Review
