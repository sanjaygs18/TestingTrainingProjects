from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID,"email")
edit_box.send_keys("shyam143pr@gmail.com")
#edit_box.send_keys(Keys.RETURN)


edit_box = driver.find_element(By.ID,"passwd")
edit_box.send_keys("Sam@pr9493!")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

#driver.find_element(By.ID, "SubmitLogin").click()
#time.sleep(5)