from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(5)

try:
    action1 = ActionChains(driver)
    action1.move_to_element(driver.find_element(By.CLASS_NAME,"lang"))
    print("Mouse hovered to English button")
    time.sleep(3)
    link = driver.find_element(By.XPATH,"(//span[contains(text(),'Deutschland')])[2]")
    action1.move_to_element(link).click()
    print("Item clicked")

except:
    print("Mouse Hover failed ")



