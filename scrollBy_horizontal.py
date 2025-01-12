from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

baseURL = "https://jqueryui.com/slider/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)
time.sleep(5)
driver.implicitly_wait(5)

driver.switch_to.frame(0)
element = driver.find_element(By.XPATH,"//div[contains(@id,'slider')]")

try:
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(element,400,0)
    print("Sliding Element Successful")
except:
    print("Sliding failed on element")