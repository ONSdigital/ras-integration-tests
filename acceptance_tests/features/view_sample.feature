Feature: View sample
   As a Collection Exercise Coordinator
   I need to understand the content of a sample
   So that I am reasonably assured that it is the right sample file for the collection exercise

  Scenario: View sample in context of the specific collection exercise
    Given the user has loaded the sample in context of 1803 collection exercise for the QBS
    When the internal user navigates to the collection exercise details page for QBS 1803
    Then the user is able to view the sample loaded for that collection exercise
    And the internal user signs out