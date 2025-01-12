from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()
time.sleep(5)

all_links = driver.find_elements(By.XPATH,".//a")
print(len(all_links))

for link in all_links:
    print(link.text,end=" - ")
    if link.get_attribute("href"):
        print("Link is present")
    else:
        print("Link is not present")

footer_links = driver.find_elements(By.XPATH,"//div[@class='footer-upper-wrapper']//a")
print(len(footer_links))

for flinks in footer_links:
    print(flinks.text, end= " - ")
    if flinks.get_attribute("href"):
        print("link is present")
    else:
        print("Link is not present")