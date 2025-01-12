Feature: Validate the login & logout functionality

  Scenario: Verifying or the login & logout features using valid test data
    Given : User should launch the chrome browser
    When : User should enter the valid URL
    When : User should enter the valid email address and password in the textboxes
    And : User should click on login push button
    Then : User should be navigated to homepage
    And : User should close the browser
