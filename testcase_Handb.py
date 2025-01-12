from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('User should launch the chrome browser')
def launchBrowserhandb(context):
    context.driver = webdriver.Chrome()

@When("User should enter the valid URL")
def enterUrlhandb(context):
    context.driver.get("https://auth.hollandandbarrett.com/u/login")
    time.sleep(5)

@When("User should enter the valid email address and password in the textboxes")
def enterKeyshandb(context):
    context.driver.find_element(By.NAME,"username").send_keys("sanjay.saimurali18@gmaul.com")
    context.driver.find_element(By.ID,"password").send_keys("H&b@1897")
    time.sleep(5)

@When("User should click on login push button")
def clickLoginBtnhandb(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Sign In')]").click()

@Then("User should be navigated to homepage")
def loginpagehandb(context):
    actual_title = context.driver.title
    expect_title = "Sign in - to you account for best experience"
    assert actual_title == expect_title
