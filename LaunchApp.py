from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '15'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('D:\\TestApks\\Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

# Step 2 : Create "Driver object"
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723/wd/hub",options =options)

# Step 3 : "Click on the App"
ele_id = driver.find_element(AppiumBy.ID,"com.skill2lead.appiumdemo:id/EnterValue")
ele_id.click()

# Step 4 : Wait for 2 seconds
time.sleep(2)

# Step 5 : Close the driver object
driver.quit()