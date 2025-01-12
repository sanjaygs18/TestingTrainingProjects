Feature: Validating login & Logout functionality

  Scenario: Verifying or checking the login & Logout functionalities
    Given : User should open chrome browser
    When :  User should enter the valid URl
    When : User should navigate to the login page
    And : User should enter the valid username and password in textboxes
    And : User click on login pushbutton
    Then : User should receive a message that "Login Successfully"
    And : User should close the browser