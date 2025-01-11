import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class OCLoginPage():

    def __init__(self,driver):
        self.driver = driver


    def OcLoginPage(self,emailID,password):
        self.driver.find_element(By.ID,"input-email").send_keys(emailID)
        self.driver.find_element(By.ID,'input-password').send_keys(password)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

