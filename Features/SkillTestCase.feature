# Created by Ademola Bhadmus at 09/03/2020
Feature: The Skill or Tool Addition Script
  This is a test script that simulates adding a skill or tool on the MyAndela web page

  Scenario: Steps To Add a New Skill or Tool
    Given I am on the login page for the myandela app
    When I insert my login with valid details
    And I click the Sign In button
    And I click on add new skill
    And I fill in the details
    And I click the Add Skill button
    Then It should add successfully