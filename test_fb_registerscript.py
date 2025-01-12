import unittest
import pytest
from selenium import webdriver
from Facebook.actions import Basicactions
from Facebook.Login_page import Loginpage
from Facebook.register_page import Registerpage
import unittest

class Fb_testscripts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.close()

    def test_login(self):
        self.driver.get("https://www.facebook.com/")
        login = Loginpage(self.driver)
        login.enterlogindetails("","")
        login.clickonloginbtn()