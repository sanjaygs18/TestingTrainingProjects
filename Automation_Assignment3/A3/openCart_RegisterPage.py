import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest


class OcRegisterPage:

    def __init__(self,driver):
        self.driver = driver
        self.driver = webdriver.Firefox()


    def maxNameCheck(self):
        Fname = self.driver.find_element(By.ID,"input-firstname")
        Fname_maxLength = Fname.get_attribute("max_length")
        self.fnMax_input = random.choices(string.ascii_letters, string.digits,Fname_maxLength+1)
        Lname = self.driver.find_element(By.ID,"input-lastname")
        Lname_maxLength = Lname.get_attribute("max_length")
        self.lnMax_input = random.choices(string.ascii_letters,string.digits,Lname_maxLength+1)
        return self.fnMax_input,self.lnMax_input


    def personalDetails(self,FnInput,LnInput,emailID,password,privacyInput,newsletterInput):
        self.driver.find_element(By.ID,"input-firstname").send_keys(FnInput)
        self.driver.find_element(By.ID,"input-lastname").send_keys(LnInput)
        self.driver.find_element(By.ID,"input-email").send_keys(emailID)
        self.driver.find_element(By.ID,"input-password").send_keys(password)
        if privacyInput.lower() == "yes":
            self.driver.find_element(By.CLASS_NAME,"btn-primary").click()
        if newsletterInput.lower() == "yes":
            self.driver.find_element(By.ID,"input-newsletter").click()

    def clickoncontinue(self):
        self.driver.find_element(By.ID,"btn-primary").click()

    def clickOnViewMyOrders(self):
        self.driver.find_element(By.LINK_TEXT,"View your order history").click()



