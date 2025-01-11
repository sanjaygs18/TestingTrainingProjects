from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    email_loc = (By.ID, "input-email")
    password_loc = (By.ID, "input-password")
    loginbtn_loc = (By.CSS_SELECTOR, "//input[@type='submit']")

    def login(self, email, password):
        self.driver.find_element(self.email_loc).send_keys(email)
        self.driver.find_element(self.password_loc).send_keys(password)
        self.driver.find_element(self.loginbtn_loc).click()
