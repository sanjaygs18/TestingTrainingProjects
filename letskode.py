from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID,"email")
edit_box.send_keys("sanjay.saimurali18@gmail.com")
edit_box.send_keys(Keys.RETURN)


edit_box = driver.find_element(By.NAME,"password")
edit_box.send_keys("Letskode@1897")
#edit_box.send_keys(Keys.RETURN)
time.sleep(5)

button = driver.find_element(By.XPATH,"//*[@id=\"login\"]").click()