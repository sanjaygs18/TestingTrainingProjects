import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddItemsToCart():

    def __init__(self,driver):
        self.driver = driver

    def getIntoVitaminsSec(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Vitamins & Supplements").click()
        self.driver.find_element(By.XPATH,"//button[@class='CategoryButtonsHP-module_carouselItem__p8SXL  '][contains(.,'Vitamins')]").click()
        self.driver.find_element(By.XPATH, "//a[@aria-label='Link to Vitamin C category']").click()

    def vitaminsItems(self,vitaminsCssSelectorPath):
        productAttributes = self.driver.find_element(By.CSS_SELECTOR,vitaminsCssSelectorPath)
        splitProAttributes = [productAttributes.text]
        individualAttributes = splitProAttributes[0].split('\n')
        self.vitaminName = individualAttributes[2]
        self.vitaminprice = individualAttributes[4]
        productAttributes.get_attribute("value = Add to Basket").click()
        self.vitaminquantity = self.driver.find_element(By.ID,"quantity").get_attribute("value")
        print(f"The {self.vitaminName} costs {self.vitaminprice} per unit")
        self.driver.back()
        return self.vitaminName,self.vitaminprice,self.vitaminquantity


    def getIntoVeganItems(self):
        self.driver.find_element(By.XPATH,"//a[contains(@class,'CategoryButtonsHP-module_carouselItem__FyNEN  CategoryButtonsHP-module_lastItem__UwN1J')]").click()

    def veganItems(self,veganCssSelectorPath):
        productAttributes = self.driver.find_element(By.CSS_SELECTOR,veganCssSelectorPath)
        splitProAttributes = [productAttributes.text]
        individualAttributes = splitProAttributes[0].split('\n')
        self.veganName = individualAttributes[1]
        self.veganPrice = individualAttributes[3]
        productAttributes.click()
        self.veganquantity = self.driver.find_element(By.ID,"quantity").get_attribute("value")
        print(f"The {self.veganName} costs {self.veganPrice} per unit")
        self.driver.back()
        return  self.veganName,self.veganPrice,self.veganPrice







