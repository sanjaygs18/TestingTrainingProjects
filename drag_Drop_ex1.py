from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

#Open a browser and launch the URL
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(8)

#find the target elements(draggable & droppable) you want to drag&drop
driver.switch_to.frame(0)
fromElement = driver.find_element(By.ID,"draggable")
toElement = driver.find_element(By.ID,"droppable")

#Perform action - drag the draggable element and drop it over the droppable area
action = ActionChains(driver)
action.drag_and_drop(fromElement,toElement).perform()

