from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/campaign/landing.php")
driver.maximize_window()
time.sleep(5)

dropdown = driver.find_element(By.ID,"month")
mon = Select(dropdown)
time.sleep(5)

no_of_mon = len(mon.options)
print(f'There are {no_of_mon} options under month list box')

for option in mon.options:
    print(option.text)
mon.select_by_visible_text("Aug")