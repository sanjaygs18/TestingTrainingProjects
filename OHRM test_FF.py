from selenium import webdriver
import time
driver1 = webdriver.Firefox()
driver1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver1.maximize_window()
time.sleep(5)
driver1.minimize_window()
time.sleep(8)
actual_title = driver1.title
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print ("Title matched")
else:
    print("Title not matched")
c_url = driver1.current_url
print(" The current URL is " +c_url)
print(c_url.title())
print(len(c_url.title()))
print(driver1.page_source.encode("utf-8"))
print(len(driver1.page_source.encode("utf-8")))