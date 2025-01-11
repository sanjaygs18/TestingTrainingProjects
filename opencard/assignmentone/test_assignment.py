import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from opencard.assignmentone.home_page import HomePage
from opencard.assignmentone.register_page  import RegisterPage
from opencard.assignmentone.address_page import AddressPage
import unittest

class OpenCartCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://demo.opencart.com.gr/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_homepage_title(self):
        self.driver.get("https://demo.opencart.com.gr/")
        expected_title = "Your Store"
        actual_title = self.driver.find_element(By.LINK_TEXT,"Your Store").text
        assert actual_title == expected_title

    def test_register_page_title(self):
        self.home_page.getintoRegisterPage()
        expected_title = "Register Account"
        actual_title = self.driver.title
        assert actual_title == expected_title

    def test_privacy_warning_alert(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        register_page.personalDetails("", "", "", "", "no", 'no',"", "")
        register_page.clickoncontinue()
        expected_alert = "Warning: You must agree to the Privacy Policy!"
        # actual_alert = self.driver.find_element(By.ID,"alert").text
        actual_alert = self.driver.find_element(By.CLASS_NAME, "alert").text
        assert actual_alert == expected_alert


    def test_first_name_required_input(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        register_page.personalDetails("", "", "", "", "no", 'no',"", "")
        register_page.clickoncontinue()
        expected_alert = "First Name must be between 1 and 32 characters!"
        # actual_alert = self.driver.find_element(By.ID,"alert").text
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_first_name_max_input(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name = register_page.get_max_input_values(34)
        register_page.personalDetails(first_name, "", "", "", "no", 'no',"", "")
        register_page.clickoncontinue()
        expected_alert = "First Name must be between 1 and 32 characters!"
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_last_name_max_input(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name =  register_page.get_max_input_values(32)
        last_name = register_page.get_max_input_values(34)

        register_page.personalDetails(first_name, last_name, "", "", "no", 'no', "", "")
        register_page.clickoncontinue()
        expected_alert = "Last Name must be between 1 and 32 characters!"
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_valie_email_input(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name =  register_page.get_max_input_values(32)
        last_name = register_page.get_max_input_values(32)
        email = "test@test"

        register_page.personalDetails(first_name, last_name, email, "", "no", 'no',"", "")
        register_page.clickoncontinue()
        expected_alert = "E-Mail Address does not appear to be valid!"
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_phone_min_max_input(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name =  register_page.get_max_input_values(32)
        last_name = register_page.get_max_input_values(32)
        email = "test@test.com"
        phone =  register_page.get_max_input_values(33)
        register_page.personalDetails(first_name, last_name, email, "", "no", 'no', phone,"")
        register_page.clickoncontinue()
        expected_alert = "Telephone must be between 3 and 32 characters!"
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_password_min_input(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name =  register_page.get_max_input_values(32)
        last_name = register_page.get_max_input_values(32)
        email = "test@test.com"
        phone =  "1234567890"
        password = register_page.get_max_input_values(3)
        register_page.personalDetails(first_name, last_name, email, password, "no", 'no',phone, "")
        register_page.clickoncontinue()
        expected_alert = "Password must be between 4 and 20 characters!"
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_confirm_password_match(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name =  register_page.get_max_input_values(32)
        last_name = register_page.get_max_input_values(32)
        email = "test@test.com"
        phone =  "1234567890"
        password = register_page.get_max_input_values(20)
        register_page.personalDetails(first_name, last_name, email, password, "no", 'no', phone, "1234567")
        register_page.clickoncontinue()
        expected_alert = "Password confirmation does not match password!"
        actual_alert = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        assert actual_alert == expected_alert

    def test_registration_successful(self):
        self.home_page.getintoRegisterPage()
        register_page = RegisterPage(self.driver)
        first_name =  register_page.get_max_input_values(32)
        last_name = register_page.get_max_input_values(32)
        email = "test_2@test.com"
        phone =  "1234567890"
        password = register_page.get_max_input_values(20)
        register_page.personalDetails(first_name, last_name, email, password, "Yes", 'Yes', phone, password)
        register_page.clickoncontinue()
        expected_alert = "Congratulations! Your new account has been successfully created!"
        actual_alert = self.driver.find_element(By.XPATH, "//*[@id=\"content\"]/p[1]")
        time.sleep(15)
        assert actual_alert == expected_alert

    # def test_SuccessfulRegistration(self):
    #     test3 = OcHomePage(self.driver)
    #     test3.getintoRegisterPage()
    #     test3 = OcRegisterPage(self.driver)
    #     test3.personalDetails("Steve","gates","trillionaresteve.123@gmail.com","yes","yes")
    #     expected_alert = "Your Account Has Been Created!"
    #     actual_alert = self.driver.title
    #     assert expected_alert == actual_alert
    #     test3.clickoncontinue()
    #     test3.clickOnViewMyOrders()
    #     test3 = addressPage(self.driver)
    #     test3.getIntoAddressPage("Steve","gates","Road no. 36","Banglore","560033","India","Karnataka","No")

if __name__ == "__main__":
    unittest.main()