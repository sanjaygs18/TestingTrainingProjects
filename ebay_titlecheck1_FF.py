from selenium import webdriver
import time
driverobj = webdriver.Firefox()
driverobj.get("https://www.ebay.com/")
driverobj.maximize_window()
time.sleep(5)
driverobj.minimize_window()
time.sleep(8)
actual_title = driverobj.title
expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
if actual_title == expected_title:
    print("Title matched")
else:
    print("Title not matched")
c_url = driverobj.current_url
print(" The current URL is " +c_url)
print(c_url.title())
print(len(c_url.title()))
print(driverobj.page_source.encode("utf-8"))
print(len(driverobj.page_source.encode("utf-8")))