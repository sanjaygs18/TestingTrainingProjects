from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")
driver.maximize_window()
time.sleep(5)

text_box = driver.find_element(By.ID,"log_email")
text_box.send_keys("8838540940")
#text_box.send_keys(Keys.RETURN)

text_box = driver.find_element(By.NAME,"log_password")
text_box.send_keys("Hiox@1897")
text_box.send_keys(Keys.RETURN)
time.sleep(5)
