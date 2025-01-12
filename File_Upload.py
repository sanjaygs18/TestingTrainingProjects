import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(8)

driver.execute_script("window.scrollBy(0,1300);")
driver.find_element(By.ID,"singleFileInput").send_keys("C://Selenium_training//program_screenshots//FirstStep.png")
#driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(5)

#element.send_keys("C://Selenium_training//program_screenshots//FirstStep.JPG")
#time.sleep(5)