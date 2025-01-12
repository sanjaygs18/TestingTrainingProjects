from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.rajasthanroyals.com/login")
driver.maximize_window()
time.sleep(5)

element = driver.find_element(By.CLASS_NAME,"nav-anchor")
itemToClickLocator = "//span[@class='nav-text'][contains(.,'Squad')]"


try:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    #ActionChains(driver).move_to_element().perform()
    print("Mouse handovered on 'Squad' element")
    time.sleep(3)
    toplink = driver.find_element(By.XPATH,itemToClickLocator)
    actions.move_to_element(toplink).click().perform()

    print("Item Clicked")
except:
    print("mouse hover failed on element")
