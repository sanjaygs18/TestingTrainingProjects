from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self,driver):
        self.driver = driver

    search_loc = (By.NAME, "search")
    searchbtn_loc = (By.CSS_SELECTOR, ".input-group-btn")
    proDescriptionCheckBox = (By.XPATH,"//label[normalize-space()='Search in product descriptions']")
    searchbtn2_loc = (By.ID,"button-search")
    product_loc = (By.LINK_TEXT, "HTC Touch HD")
    qty_loc = (By.NAME, "quantity")
    AddtoCartBtn = (By.ID, "button-cart")
    successmsg_loc = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def search_product(self, product_name):
        self.driver.find_element(self.search_loc).send_keys(product_name)
        self.driver.find_element(self.searchbtn_loc).click()
        self.driver.find_element(self.proDescriptionCheckBox).click()
        self.driver.find_element(self.searchbtn2_loc).click()

    def select_product(self):
        self.driver.find_element(self.product_loc).click()

    def update_quantity_and_add_to_cart(self, quantity):
        self.driver.find_element(self.qty_loc).send_keys(quantity)
        self.driver.find_element(self.AddtoCartBtn).click()

    def get_success_message(self):
        return self.driver.find_element(self.successmsg_loc)
