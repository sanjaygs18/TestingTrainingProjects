from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import XLUtilities

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()

path = "C://SeleniumPractice/LoginTest.xlsx"

rows = XLUtilities.getRowCount(path,"Sheet1")
print(rows)

for r in range(2,rows+1):
    username = XLUtilities.readData(path,"Sheet1",r,1)
    password = XLUtilities.readData(path,"Sheet1",r,2)

    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='button'][contains(.,'Login')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH,"//img[contains(@class,'zl-navbar-rhs-img ')]").click()
    driver.find_element(By.XPATH,"//a[contains(.,'Logout')]").click()
    time.sleep(10)

    if driver.title == "Home Page":
        print("Test is Passed")
        XLUtilities.writeData(path,"Sheet1",r,3,"Passed")
    else:
        print("Test is Failed")
        XLUtilities.writeData(path,"Sheet1",r,3,"Failed")

    driver.find_element(By.XPATH,"//a[contains(@href,'login')]").click()

