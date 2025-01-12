from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
time.sleep(3)


driver.find_element(By.LINK_TEXT,"Women").click()
time.sleep(3)

ddown1 = driver.find_element(By.ID,"selectProductSort")
var = Select(ddown1)
time.sleep(3)

print(f"No of options available in women list box is {len(var.options)}")
for i in var.options:
    print(i.text)



