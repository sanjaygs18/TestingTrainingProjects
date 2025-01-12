import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.select import Select


class AddressPage():

    def __init__(self,driver):
        self.driver = driver

    def getIntoAddressPage(self,FnInput,LnInput,Address,City,postcode,countryName,region,defaultAddressInput):
        self.driver.find_element(By.XPATH,"	//a[contains(text(),'Address Book')]").click()
        self.driver.find_element(By.LINK_TEXT,"New Address").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys(FnInput)
        self.driver.find_element(By.ID, "input-lastname").send_keys(LnInput)
        self.driver.find_element(By.ID, "input-address-1").send_keys(Address)
        self.driver.find_element(By.ID, "input-city").send_keys(City)
        self.driver.find_element(By.ID, "input-postcode").send_keys(postcode)
        dropdown = self.driver.find_element(By.ID, "input-country")
        Country = Select(dropdown).select_by_value(countryName)
        dropdown = self.driver.find_element(By.ID, "input-zone")
        Region = Select(dropdown).select_by_value(region)
        if defaultAddressInput == "yes":
            self.driver.find_element(By.ID,"input-default-yes").click()

        else:
            self.driver.find_element(By.ID,"input-default-no").click()
        self.driver.find_element(By.ID,"//button[@type='submit']").click()



