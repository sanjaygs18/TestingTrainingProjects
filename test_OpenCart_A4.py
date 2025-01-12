from selenium.webdriver.common.by import By
from selenium import webdriver
from Automation_Assignment3.A3.openCart_RegisterPage import OcRegisterPage
from Automation_Assignment3.A3.openCart_Homepage import OcHomePage
import unittest
from Automation_Assignment3.A3.openCart_AddressPage import addressPage

class OpenCartCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.close()


    def test_privacyCheck(self):
        self.driver.get("https://demo.opencart.com.gr/")
        test0 = OcHomePage(self.driver)
        test0.getintoRegisterPage()
        test0 = OcRegisterPage(self.driver)
        test0.personalDetails("","","","","no",'no')
        test0.clickoncontinue()
        expected_alert = "Warning: You must agree to the Privacy Policy!"
        actual_alert = self.driver.find_element(By.ID,"alert").text
        assert actual_alert == expected_alert


    def test_FirstNameCheck(self):
        test1 = OcHomePage(self.driver)
        test1.getintoRegisterPage()
        test1 = OcRegisterPage(self.driver)
        fn_max = test1.fnMax_input
        test1.personalDetails(fn_max,"abcd","abcd.1897@gmail.com","Abc@123","yes","yes")
        actual_alert = self.driver.find_element(By.ID,"error-firstname").get_attribute("value")
        expected_alert = "First Name must be between 1 and 32 characters!"
        assert actual_alert.strip == expected_alert

    def test_LastNameCheck(self):
        test2 = OcHomePage(self.driver)
        test2.getintoRegisterPage()
        test2 = OcRegisterPage(self.driver)
        ln_max = test2.lnMax_input
        test2.personalDetails("Pqrs",ln_max,"qwerty.123@gmail.com","Wasd@123","yes","yes")
        expected_alert = "Last Name must be between 1 and 32 characters!"
        actual_alert = self.driver.find_element(By.ID,"error-lastname").get_attribute("value")
        assert actual_alert == expected_alert

    def test_SuccessfulRegistration(self):
        test3 = OcHomePage(self.driver)
        test3.getintoRegisterPage()
        test3 = OcRegisterPage(self.driver)
        test3.personalDetails("Steve","gates","trillionaresteve.123@gmail.com","yes","yes")
        expected_alert = "Your Account Has Been Created!"
        actual_alert = self.driver.title
        assert expected_alert == actual_alert
        test3.clickoncontinue()
        test3.clickOnViewMyOrders()
        test3 = addressPage(self.driver)
        test3.getIntoAddressPage("Steve","gates","Road no. 36","Banglore","560033","India","Karnataka","No")

if __name__ == "__main__":
    unittest.main()