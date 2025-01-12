from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://auth.hollandandbarrett.com/u/login")
time.sleep(8)

edit_box = driver.find_element(By.ID,"username")
edit_box.send_keys("sanjay.saimurali18@gmail.com")
edit_box.send_keys(Keys.RETURN)
driver.save_screenshot("C:\Selenium_training\program_screenshots//FirstStep.png")

edit_box1 = driver.find_element(By.NAME,"password")
edit_box1.send_keys("H&B@1897")
#edit_box.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element(By.XPATH,"//button[contains(text(),'Sign In')]").click()
time.sleep(5)
driver.save_screenshot("C:\Selenium_training\program_screenshots//SecondStep.png")

driver.save_screenshot("C:\Selenium_training\program_screenshots//error msg.png")
destinationFilename = "C:\Selenium_training\program_screenshots.//screenshot.png"

fileName = str(round(time.time()*1000))+".png"
screenshotDirectory = "C:\Selenium_training\program_screenshots.//screenshot.png"
destinationFile = screenshotDirectory+fileName

try:
    driver.save_screenshot(destinationFile)
    print("Screenshot saved to  directory --> ::"+destinationFile)
except NotADirectoryError:
    print("Not a directory issue")
