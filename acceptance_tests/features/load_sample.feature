Feature: Load sample
   As a Collection Exercise Coordinator
   I need to be able to load the sample
   So that a sample file exists in the system

     Scenario: Load sample
     Given the 1803 collection exercise for the QBS survey has been created
     When the internal user navigates to the collection exercise details page
     Then the user is able to load the sample