from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(5)

text_box = driver.find_element(By.ID,"username")
text_box.send_keys('sanjay.saimurali18@gmail.com')
text_box.send_keys(Keys.RETURN) #Enter values in edit box by press keyword

text_box = driver.find_element(By.NAME,"password").size
#text_box.send_keys("H&B@1897")
#text_box.send_keys(Keys.RETURN) #Enter values in edit box by press keyword
print(text_box)
print(text_box['width'])