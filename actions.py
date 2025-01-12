from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Basicactions:

    def __init__(self,driver):
        self.driver = driver

    def wait_and_click(self,locators):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locators))
        element.click()

    def enter_values_in_the_element(self,locators,value):
        print(type(locators))
        entertxt = self.driver.find_element((locators))
        entertxt.clear()
        entertxt.send_keys(value)

