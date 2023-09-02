import time
import unittest
from selenium import webdriver
from AT_Project2.Page.tc_pim_01_password_validation_page import ResetPassword


class LoginPagePasswordValidation(unittest.TestCase):
    # initializing the driver.
    driver = None

    # Setupclass method run only once before all test cases.
    @classmethod
    def setUpClass(cls) -> None:
        print("Launching my browser before all my test cases start running")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    @classmethod
    def tearDownClass(cls) -> None:
        print("I am after the test class")

    # Tests case_ID  : TC_PIM_01 -Forgot password link validation
    # Created object of password validation page and performing testing whether reset
    # password link sent successfully message is displaying or not

    def test_forgot_password_link_validation(self):
        loginobject = ResetPassword(self.driver)
        loginobject.click_forgot_password_link()
        loginobject.input_username_for_reset_password()
        loginobject.click_on_reset_button()
        assert loginobject.verify_reset_password_link_message_displaying()
        time.sleep(20)
