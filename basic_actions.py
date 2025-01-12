from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = self.driver.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.driver.find_element(locator)
        return element.text
