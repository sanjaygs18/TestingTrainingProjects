from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import time

#launch chrome browser & enter the URL
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(3)

driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[2]/div[2]/div[1]/input[2]").click()
time.sleep(2)

t = driver.switch_to.alert.text
print(t)
driver.switch_to.alert.accept()


driver.get("https://www.ksrtc.in/login")
w = WebDriverWait(driver,5)

#driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[4]").click()
e1 = w.until(expected_conditions.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[4]")))
e1.click()



