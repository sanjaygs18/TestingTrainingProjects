from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


#User should open browser and launch URL
baseURL = "https://www.letskodeit.com/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)
time.sleep(5)

#Count number Radio buttons and Check boxes and print
noofRadioBtn = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(f"The number of radio button {len(noofRadioBtn)} and they are")
for button in noofRadioBtn:
    print(button.get_attribute("value"),end = " ")
print('\n')
noofCheckBox = driver.find_elements(By.XPATH, "//input[@type='checkbox'][@name ='cars']")
print(f"The number of checkbox {len(noofCheckBox)} and they are")
for button in noofCheckBox:
    if button.get_attribute("name") == "cars":
        print(f"\n {button.get_attribute("value")}",end = " ")
print('\n')
#Move hand over on "Mouse Hover" then click on 'Reload'
try:
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CLASS_NAME,"dropbtn")).click().perform()
    reloadlink = driver.find_element(By.XPATH,"//a[contains(.,'Reload')]")
    action.move_to_element(reloadlink).click().perform()
    time.sleep(5)
    element = driver.find_element(By.XPATH, "//button[@id='mousehover']")
    driver.execute_script('arguments[0].scrollIntoView(true);', element)
    driver.save_screenshot(".//mousehoverscreenshot.png")
    print("Item Clicked")

except:
    print("Mouse hover not performed")

#Enter "Selenium Python" in Editbox Validate both Alerts
driver.find_element(By.XPATH,"//div[@id='alert-example-div']//input[@id='name']").send_keys("Selenium Python")
driver.find_element(By.ID  ,"alertbtn").click()
time.sleep(5)

driver.switch_to.alert.accept()
time.sleep(5)
driver.save_screenshot(".//simplealert.png")

driver.find_element(By.XPATH,"//input[contains(@name,'enter-name')]").send_keys("Selenium Python")
driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
time.sleep(5)

driver.switch_to.alert.accept()
time.sleep(5)
driver.save_screenshot(".//confirmalertaccept.png")

driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()

driver.switch_to.alert.dismiss()
#WebDriverWait(driver,5)
driver.save_screenshot(".//confirmalertdismiss.png")

#Print Page Title, Get page Source and Page Source length
print(f"The title of the page is \"{driver.title}\"")
print(f"The PageSource of the page is \" {driver.page_source.encode("utf-8")}\"")
print(f"Length of page source is \" {len(driver.page_source)}\"")

#Validate the title with "Practice Page"
if driver.title == "Practice Page":
    print("Title Matches")
else:
    print("Title doesnot match")

#Click Terms and Conditions and then Click Sign in enter proper credentials then sign in
driver.find_element(By.LINK_TEXT,"Terms & Conditions").click()
driver.save_screenshot(".//T&C.png")
driver.back()

driver.find_element(By.XPATH,"//a[normalize-space()='Sign In']").click()
time.sleep(3)
driver.save_screenshot(".//signin.png")
driver.find_element(By.ID,"email").send_keys("sanjay.saimurali18@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Letskode@1897")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@id='login']").click()
time.sleep(5)
driver.save_screenshot(".//loginin.png")

driver.quit()


