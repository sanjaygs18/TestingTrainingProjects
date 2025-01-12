from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

@Given("User should open the chrome browser")
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()

@When("User should enter the valid URL")
def EnterURL(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    time.sleep(5)

@When("User should navigate to the login page of orangeHRM")
def navigate(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@When("User should enter the validate the username and password")
def enterValues(context):
    context.driver.find_element(By.NAME,"username").send_keys("Admin")
    context.driver.find_element(By.NAME,"password").send_keys("admin123")

@when("User should click on login pushbutton")
def clickloginbtn(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Login')]").click()

@Then("User should receive an message that Login Successful")
def step_imp1(context):
    status = context.driver.title
    expect_title = "OrangeHRM"
    assert status == expect_title

@Then("User should close the browser")
def logoutApp(context):
    context.driver.quit()
