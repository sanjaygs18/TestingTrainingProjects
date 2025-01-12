import unittest
from selenium import webdriver
from Automation_Assignment3.A4.OC_HomePage import HomePage
from Automation_Assignment3.A4.OC_LoginPage import LoginPage
from Automation_Assignment3.A4.OC_ComponentsPage import ComponentsPage
from Automation_Assignment3.A4.OC_CartPage import CartPage
from Automation_Assignment3.A4.OC_ProductPage import ProductPage


class OpenCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://demo.opencart.com.gr")
        self.driver.implicitly_wait(10)

    def test_opencart_workflow(self):
        hp = HomePage(self.driver)
        hp.go_to_login()

        lp = LoginPage(self.driver)
        lp.login("qwerty.123@gmail.com","Wasd@123")

        hp.navigate_to_monitors()
        cp = ComponentsPage(self.driver)
        cp.select_show_limit("25")
        cp.add_first_item_to_cart()

        pp = ProductPage(self.driver)
        pp.go_to_specifications()
        pp.add_to_wishlist()
        alert_message = pp.get_alert_message()
        assert "Success: You have added" in alert_message

        ca_p = CartPage(self.driver)
        ca_p.search_product("Mobile")
        ca_p.select_product()
        ca_p.update_quantity_and_add_to_cart("3")
        success_message = ca_p.get_success_message()
        assert "Success: You have added HTC Touch HD to your shopping cart!" in success_message


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
