from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ComponentsPage:

    def __init__(self,driver):
        self.driver = driver

    showDropDown_Loc = (By.ID, "input-limit")
    AddtoCartBtn = (By.XPATH, "//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[1]")

    def select_show_limit(self, limit_value):
        dropdown = self.driver.find_element(self.showDropDown_Loc).click()
        show = Select(dropdown).select_by_value(limit_value)

    def add_first_item_to_cart(self):
        self.driver.find_element(self.AddtoCartBtn).click()
