from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(8)


fromElement = driver.find_element(By.XPATH,"//div[@class='ui-widget-content ui-draggable ui-draggable-handle'][contains(.,'Drag me to my target')]")
toElement = driver.find_element(By.ID,"droppable")
driver.execute_script("scrollBy(0,1500);")

#driver.execute_script("arguments[0].scrollToView(true);",toElement)

actions = ActionChains(driver)
actions.drag_and_drop(fromElement,toElement).perform()