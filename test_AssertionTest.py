import unittest #file name must test_or ends with_test
import pytest
import self
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        TitleofBrowser = driver.title
        self.assertTrue(TitleofBrowser== "Google")
        #self.assertfalse(TitleofBrowser == "Google123")

if __name__ == "__main__":
    unittest.main()
