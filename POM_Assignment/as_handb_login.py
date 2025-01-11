from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

class LoginPageHB():

    def __init__(self,driver):
        self.driver = driver

    _emailAddress_ = "//input[@id='username']"
    _password_ = "//input[@id='password']"
    _loginButton_ = "//button[normalize-space()='Sign In']"

    def getEmailAddress(self,emailId):
        self.emailElement = self.driver.find_element(By.XPATH,self._emailAddress_)
        self.emailElement.send_keys(emailId)

    def getPassword(self,password):
        self.passwordElement = self.driver.find_element(By.XPATH,self._password_)
        self.passwordElement.send_keys(password)

    def getlogin(self):
        self.loginElement = self.driver.find_element(By.XPATH,self._loginButton_).click()
        #self.loginElement.click()

    def loginhandb(self, emailid, password):
        self.getEmailAddress(emailid)
        self.getPassword(password)
        self.getlogin()


