import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OcHomePage():

    def __init__(self,driver):
        self.driver = driver

    MyAccBtn = "//span[contains(text(),'My Account')]"
    registerBtn = "//a[contains(text(),'Register')]"

    def getintoRegisterPage(self):
        self.driver.find_element(By.XPATH,self.MyAccBtn).click()
        self.driver.find_element(By.XPATH,self.registerBtn).click()

    def getintoLoginPage(self):
        self.driver.find_element(By.XPATH, self.MyAccBtn).click()
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()


