from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/section[1]/span[1]"))).click()
traveller = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.lbl_input.appendBottom5")))
traveller.click()
no_of_travellers = Select(traveller)
for number in no_of_travellers.options:
    print(number.text)

