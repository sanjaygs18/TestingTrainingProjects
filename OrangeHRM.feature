Feature: Login & Logout functionality check

Scenario: Verify or Checking the orangeHRM login & logout application
      Given User should open the chrome browser
      When User should enter the valid URL
      And User should navigate to the login page of orangeHRM
      And User should enter the validate the username and password
      And User should click on login pushbutton
      Then User should receive an message that Login Successful
      Then User should close the browser

