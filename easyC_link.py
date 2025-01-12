from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//a[normalize-space()='Love Calculator']").click()
time.sleep(5)

ad_e = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,"adsbygoogle adsbygoogle-noablate"))
c_button = driver.find_element(By.XPATH,'//*[@id="dismiss-button"]')