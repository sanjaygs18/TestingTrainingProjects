from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(5)

#driver.switch_to.alert.dismiss()
driver.execute_script("window.scrollBy(0,2000);")
time.sleep(2)

driver.execute_script("window.scrollBy(0,-1900);")
time.sleep(2)

element1 = driver.find_element(By.CSS_SELECTOR,".css-1dbjc4n r-11wnrd2 r-18u37iz")
driver.execute_script("arguments[0].scrollIntoView(true);",element1)
time.sleep(3)
driver.execute_script("window.scrollBy(0,-150);")

driver.find_element(By.CSS_SELECTOR,".css-1dbjc4n r-11wnrd2 r-18u37iz").click()
time.sleep(3)