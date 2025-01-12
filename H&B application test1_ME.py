from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(8)
actual_title = driver.title
expect_title = "Sign in - to your account, for the best experience"

if actual_title == expect_title:
    print("Title Match")
else:
    print("Title not match")
c_url = driver.current_url
print(" The current URL is " +c_url)
print(c_url.title())
print(len(c_url.title()))
print(driver.page_source.encode("utf-8"))
print(len(driver.page_source.encode("utf-8")))