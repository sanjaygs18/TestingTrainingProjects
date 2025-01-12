from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollBy(0,1000);")
time.sleep(5)

driver.execute_script("window.scrollBy(0,-1000);")
time.sleep(5)

element = driver.find_element(By.ID,"mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(3)
driver.execute_script("window.scrollBy(0,-150);")
time.sleep(3)