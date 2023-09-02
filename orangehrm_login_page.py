
from selenium.webdriver.common.by import By


class OrangeHrmPage:

    # This is constructor of page class.
    def __init__(self,driver):
        self.loginpage_driver = driver

    # Locators of Orangehrm page
    username_locator = "username"
    password_locator = "password"
    login_locator ="//button[text()=' Login ']"

    # this method is used for entering username
    def input_username(self,username):
            self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    # this method is used for entering password
    def input_password(self, password):
            self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    # this method is used for clicking on loging button.
    def click_login_button(self):
            self.loginpage_driver.find_element(By.XPATH, self.login_locator).click()
