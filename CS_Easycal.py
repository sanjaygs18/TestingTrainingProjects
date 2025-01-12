from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Launch below URL using chrome browser
driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(5)

#Click on "Sign In" button
driver.find_element(By.XPATH, "//*[@id=\'wrap\']/div[2]/div[2]/span[2]/a/span").click()

#Enter mobile/email and password then click on login button
m_tbox = driver.find_element(By.ID,"log_email")
m_tbox.send_keys("shyam143pr@gmail.com")
#m_tbox.send_keys(Keys.RETURN)
time.sleep(5)

m_tbox = driver.find_element(By.NAME,"log_password")
m_tbox.send_keys("Sam@pr9493!")
#m_tbox.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element(By.XPATH, '//body/div[1]/div[1]/div[2]/form[1]/div[4]/input[1]').click()
time.sleep(5)

#Enter "Bangalore" in edit then click search button
tbox = driver.find_element(By.ID,"googleSearchId")
tbox.send_keys("Bangalore")
time.sleep(5)

driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/form[1]/span[2]/button[1]").click()
time.sleep(5)
