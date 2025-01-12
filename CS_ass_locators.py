from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(5)

#driver.find_element(By.XPATH, "//a[@href='//www.easycalculation.com/date-day/age-calculator.php']").click()
#time.sleep(5)

driver.find_element(By.LINK_TEXT,"Age Calculator").click()
time.sleep(3)

a_links = driver.find_elements(By.XPATH,'.//a')
for index, link in enumerate(a_links[:10],start=1):
    print(f"link{index} {link.get_attribute("href")}")

images = driver.find_elements(By.TAG_NAME,"img")
for index, img in enumerate(images[:5],start=1):
    print(f"\n image{index} {img.get_attribute("src")}")

driver.find_element(By.ID,"i21").send_keys("18")
driver.find_element(By.ID,"i22").send_keys('11')
driver.find_element(By.ID,"i23").send_keys("1997")

driver.find_element(By.XPATH,'//*[@id="dispCalcConts"]/div[3]/form/table/tbody/tr[10]/td/input[1]').click()
time.sleep(3)

print(f"Your Age is {driver.find_element(By.NAME,"val").get_attribute("value")}")
print(f"Your Age in Days is {driver.find_element(By.NAME,"val1").get_attribute("value")}")
print(f"Your Age in Hours {driver.find_element(By.NAME,"val2").get_attribute("value")}")
print(f"Your Age in Minutes {driver.find_element(By.NAME,"val3").get_attribute("value")}")

driver.find_element(By.XPATH,'//*[@id="dispCalcConts"]/div[3]/form/table/tbody/tr[10]/td/input[2]').click()
time.sleep(3)

