from selenium import webdriver
from selenium.webdriver.common.by import By
from Facebook.actions import Basicactions


class Loginpage:

    def __init__(self,driver):
        self.driver = driver

    # locators
    emailloc = By.ID,"email"
    passloc = By.NAME,"pass"
    loginbtn_loc = By.NAME,"login"

    def enterlogindetails(self,emailid,password):
        print(type(self.emailloc))
        actions = Basicactions(self.driver)
        actions.enter_values_in_the_element(self.emailloc,emailid)
        actions.enter_values_in_the_element(self.passloc,password)


    def clickonloginbtn(self):
        actions = Basicactions(self.driver)
        actions.wait_and_click(self.loginbtn_loc)

