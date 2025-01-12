Feature: Validate the login & logout functionality

  Scenario: Verifying the login & login features using valid credentials
    Given : User should launch the chrome browser
    When : User should enter the valid URl
    When : User should navigate to homepage
    And : User should click on sign-in button
    And : User should enter the valid email address and password
    Then : User should navigated to user dashboard
    And : User should close the browser
    
