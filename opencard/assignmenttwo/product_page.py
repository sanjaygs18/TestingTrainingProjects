from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self,driver):
        self.driver = driver

    specification_loc = (By.LINK_TEXT, "Specification")
    AddtoWishlistBtn = (By.XPATH, "//div[@id='product-product']//div[@class='btn-group']//button[1]")
    AlertMsg_loc = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def go_to_specifications(self):
        self.driver.find_element(self.specification_loc).click()

    def add_to_wishlist(self):
        self.driver.find_element(self.AddtoWishlistBtn).click()

    def get_alert_message(self):
        return self.driver.find_element(self.AlertMsg_loc)
