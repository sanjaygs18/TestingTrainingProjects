from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/drag_and_drop")
time.sleep(5)

fromElement = driver.find_element(By.ID,"column-a")
toElement = driver.find_element(By.ID,"column-b")

try:
    action = ActionChains(driver)
    action.drag_and_drop(fromElement,toElement).perform()
    time.sleep(5)
    action.drag_and_drop(toElement,fromElement).perform()
    time.sleep(5)
    print("Drag and Drop Element Successful")

except:
    print("Drag and Drop Element not successful")


