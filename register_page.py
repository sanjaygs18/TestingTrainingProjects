import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class RegisterPage:

    def __init__(self,driver):
        self.driver = driver

    # self.driver = webdriver.Firefox()

    def get_max_input_values(self, max_length):
        input_text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(max_length))

        return input_text

    def personalDetails(self, FnInput, LnInput, emailID, password, privacyInput, newsletterInput, phone, confirm_password):
        self.driver.find_element(By.ID,"input-firstname").send_keys(FnInput)
        self.driver.find_element(By.ID,"input-lastname").send_keys(LnInput)
        self.driver.find_element(By.ID,"input-email").send_keys(emailID)
        self.driver.find_element(By.ID,"input-password").send_keys(password)
        self.driver.find_element(By.ID,"input-telephone").send_keys(phone)
        self.driver.find_element(By.ID,"input-confirm").send_keys(confirm_password)

        if privacyInput.lower() == "yes":
            self.driver.find_element(By.NAME,"agree").click()
        if newsletterInput.lower() == "yes":
            self.driver.find_element(By.NAME,"newsletter").click()

    def clickoncontinue(self):
        # self.driver.find_element(By.ID,"btn btn-primary").click()
        self.driver.find_element(By.CLASS_NAME,"btn-primary").click()

    def clickOnViewMyOrders(self):
        self.driver.find_element(By.LINK_TEXT,"View your order history").click()



