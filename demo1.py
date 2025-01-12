from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
time.sleep(5)

bmwRadioBtn = driver.find_element(By.ID, "bmwradio")
bmwRadioBtn.click()
time.sleep(5)

benzRadioBtn = driver.find_element(By.ID, "benzradio")
benzRadioBtn.click()
time.sleep(5)
radioBtn = driver.find_elements(By.XPATH,'.//input[@type = "radio"]')
sradiobtn = str(radioBtn.is_selected())
print(f"no of radio buttons {len(sradiobtn)}")

bmwCheckBox = driver.find_element(By.ID, "bmwcheck")
bmwCheckBox.click()
time.sleep(5)

benzCheckBox = driver.find_element(By.ID, "benzcheck")
benzCheckBox.click()
time.sleep(5)

print("BMW Radio button is selected ?" + str(bmwRadioBtn.is_selected()))
print("Benz Radio button is selected ?" +str(benzRadioBtn.is_selected()))
print("BMW checkbox is selected?" + str(bmwCheckBox.is_selected()))
print("Benz checkbox is selected?" +str(benzCheckBox.is_selected()))