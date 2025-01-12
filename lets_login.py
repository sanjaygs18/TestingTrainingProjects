import pytest
import selenium.webdriver.common.by
import selenium.webdriver.common.keys
import time

class letsLoginPage():

    def __init__(self,driver):
        self.driver = driver

    _letEmail_Loc = "email"
    _letPassword_Loc = "login-password"
    _letLoginButton_loc = "//button[@type='button'][contains(.,'Login')]"

