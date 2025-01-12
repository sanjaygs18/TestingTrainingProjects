from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    myaccount = (By.CSS_SELECTOR,"a[title='My Account'] span[class='hidden-xs hidden-sm hidden-md']")
    login = (By.XPATH,"//a[contains(text(),'Login')]")
    componentoption = (By.LINK_TEXT,"Components")
    monitoroption =(By.LINK_TEXT,"Monitors (2)")

    def go_to_login(self):
        self.driver.find_element(self.myaccount).click()
        self.driver.find_element(self.login).click()

    def navigate_to_monitors(self):
        self.driver.find_element(self.componentoption).click()
        self.driver.find_element(self.monitoroption).click()


