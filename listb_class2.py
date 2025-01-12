from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/campaign/landing.php")
driver.maximize_window()
time.sleep(5)

ddown = driver.find_element(By.ID,"day")
days = Select(ddown)

print(f"There are {len(days.options)} options available in day drop down box")
time.sleep(5)
for d in days.options:
    print(d.text)

ddown = driver.find_element(By.ID,"year")
years = Select(ddown)

print(f"There are {len(years.options)} options arr avaialable in year drop down box")
time.sleep(5)
for y in years.options[:3]:
    print(y.text)

