from selenium import webdriver
import time
import unittest
from POM1.login_page import loginPage


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL ="https://auth.hollandandbarrett.com/u/login"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.maximize_window()
        time.sleep(5)

        lp = loginPage(driver)
        lp.login("sanjay.saimurali18@gmail.com","H&b@1897")

        actual_title = driver.title
        expect_title = "Sign in - to your account, for the best experience"

        if actual_title == expect_title:
            print("Login Successful")
        else:
            print("Login Unsuccessful")