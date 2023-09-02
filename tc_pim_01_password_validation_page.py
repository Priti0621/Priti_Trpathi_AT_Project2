
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ResetPassword:
    # Constructor of page class
    def __init__(self, driver):
        self.lgpage_driver = driver

     # Locators of login page :-
    forgot_password_link_locator = "//p[text()='Forgot your password? ']"
    username_locator = "username"
    reset_password_locator = "//button[text()=' Reset Password ']"
    reset_message_locator = "//h6[text()='Reset Password link sent successfully']"

    #  Methods to call above locators and perform actions.
    # method to click on forgot password link
    def click_forgot_password_link(self):
        self.lgpage_driver.find_element(By.XPATH, self.forgot_password_link_locator).click()

    # method to click on reset password link
    def input_username_for_reset_password(self):
        self.lgpage_driver.find_element(By.NAME, self.username_locator).send_keys("Admin")

    # method to click on reset button
    def click_on_reset_button(self):
        self.lgpage_driver.find_element(By.XPATH, self.reset_password_locator).click()

    # method to check reset passsword link sent successfully.
    def verify_reset_password_link_message_displaying(self):
        reset_message = WebDriverWait(self.lgpage_driver, 10).until(EC.presence_of_element_located((By.XPATH, self.reset_message_locator)))
        return reset_message

