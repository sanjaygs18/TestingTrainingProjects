import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.easemytrip.com/")
driver.maximize_window()
time.sleep(5)

button = driver.find_element(By.ID,"divSignInPnl")
button.click()

