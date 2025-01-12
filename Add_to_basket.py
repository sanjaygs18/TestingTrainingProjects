from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class AddToBasketPage():

    def calsubtotal(self,driver,cssselector):
        self.driver = driver
        elements = self.driver.find_elements(By.CSS_SELECTOR,".jsx-549227111.jsx-3292445181.product.has-lower-banners")
        for self.element in elements:
            self.element.get_attribute("data-test-value")
            self.element = []
        return self.element



