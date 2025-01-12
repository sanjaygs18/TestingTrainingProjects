from selenium.webdriver.common.by import By
from Automation_Assignment3.A5 import XLUtility
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demo.opencart.com.gr/")
driver.maximize_window()
driver.implicitly_wait(8)

path = "C://SeleniumPractice//OpenCartLoginTest.xlsx"

rows = XLUtility.getRowCount(path,"Sheet1")


for r in range(2, rows+1):
    firstName = XLUtility.readData(path,"Sheet1",r,1)
    lastName = XLUtility.readData(path,"Sheet1",r,2)
    email = XLUtility.readData(path,"Sheet1",r,3)
    password = XLUtility.readData(path,"Sheet1",r,4)
    time.sleep(5)

    driver.find_element(By.XPATH,"//span[@class='d-none d-md-inline'][contains(.,'My Account')]").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.XPATH,"//input[contains(@name,'agree')]").click()

    driver.find_element(By.NAME,"firstname").send_keys(firstName)
    driver.find_element(By.NAME,"lastname").send_keys(lastName)
    driver.find_element(By.NAME,"email").send_keys(email)
    driver.find_element(By.NAME,"password").send_keys(password)

    driver.find_element(By.XPATH,"//input[contains(@name,'agree')]").click()
    driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Continue')]").click()

    if driver.title == "Your Account Has Been Created!":
        print("Test passed")
        XLUtility.writeData(path,"Sheet1",r,6,"Passed")

    else:
        print("Test failed")
        XLUtility.writeData(path,"Sheet1",r,6,"Failed")


    driver.find_element(By.XPATH,"//span[@class='d-none d-md-inline'][contains(.,'My Account')]").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()