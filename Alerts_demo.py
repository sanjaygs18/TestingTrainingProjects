from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
time.sleep(3)

driver.switch_to.alert.accept()
result = driver.find_element(By.ID,"result").text
print("Value of attribute is: " + result)
assert "You successfully clicked an alert", result

driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Confirm')]").click()
time.sleep(3)

driver.switch_to.alert.accept()
result = driver.find_element(By.ID,"result").text
print("Value of attribute is: " +result)
assert "You clicked: Ok",result

driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Confirm')]").click()
time.sleep(3)

driver.switch_to.alert.dismiss()
result = driver.find_element(By.ID,"result").text
print("Value of attribute is:" +result)
assert "You clicked: Cancel", result

driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Prompt')]").click()
time.sleep(3)

driver.switch_to.alert.send_keys("Hello!! Welcome to JS Alerts")
driver.switch_to.alert.accept()
result = driver.find_element(By.ID,"result").text
print("Value of attribute is "+result)
assert "You entered: Hello!! Welcome to JS Alerts", result

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
value = driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credenti')]").text
print("Value of the attribute " +value)
assert "Congratulations! You must have the proper credentials." , value