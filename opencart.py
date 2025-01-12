from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demo.opencart.com/en-gb?route=account/login")
driver.maximize_window()
time.sleep(5)

text_box = driver.find_element(By.ID,"input-email")
text_box.send_keys("sanjay.saimurali18@gmail.com")
#text_box.send_keys(Keys.RETURN)

text_box = driver.find_element(By.NAME,"input-password  ")
text_box.send_keys("Opencart@1897")
text_box.send_keys(Keys.RETURN)
time.sleep(5)