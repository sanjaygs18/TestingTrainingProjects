import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.implicitly_wait(8)

driver.find_element(By.ID,"textbox").send_keys("Hello There! Welcome to automation!")
driver.find_element(By.ID,"createTxt").click()
driver.find_element(By.LINK_TEXT,"Download").click()

driver.find_element(By.ID,"pdfbox").send_keys("Hello There! Welcome to automation! This is of pdf format")
driver.find_element(By.ID,"createPdf").click()
driver.find_element(By.ID,"pdf-link-to-download").click()
time.sleep(5)