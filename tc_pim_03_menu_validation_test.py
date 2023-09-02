import json
import time
import unittest
from selenium import webdriver

from AT_Project2.Page.tc_pim_03_menu_validation_page import MainMenuValidation
from orangehrmpages.login_page_class import HrmLoginPage


class TitleOfMenuOptionsTestClass(unittest.TestCase):
    # initializing driver
    driver = None
    data_dict = None

    # Setupclass method run only once before all test cases.
    @classmethod
    def setUpClass(cls) -> None:
        print("Launching my chrome browser before all my test cases start running")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        hrmlpobject = HrmLoginPage(cls.driver)

        # this is json file path and loaded json data(user credentials)
        json_file_path = "C:\\Users\\Hp\\PycharmProjects\\pythonProjectLect1\\AT_Project1\\DataSource\\test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

        hrmlpobject.input_username(cls.data_dict.get("Login_test").get("correct_user_name"))
        hrmlpobject.input_password(cls.data_dict.get("Login_test").get("correct_password"))
        hrmlpobject.click_login_button()
        menu_options = MainMenuValidation(cls.driver)
        menu_options.verify_admin_is_displaying_on_menu()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # Tests case_ID  : TC_PIM_03 - Main menu validation on Admin page
    #  Created object of admin header page and executed test case.
    def test_options_displaying_on_menu_page(self):
        menu_options = MainMenuValidation(self.driver)
        assert menu_options.verify_admin_is_displaying_on_menu()
        assert menu_options.verify_pim_is_displaying_on_menu()
        assert menu_options.verify_leave_is_displaying_on_menu()
        assert menu_options.verify_time_is_displaying_on_menu()
        assert menu_options.verify_recruitment_is_displaying_on_menu()
        assert menu_options.verify_my_info_is_displaying_on_menu()
        assert menu_options.verify_performance_is_displaying_on_menu()
        assert menu_options.verify_dashboard_is_displaying_on_menu()
        assert menu_options.verify_directory_is_displaying_on_menu()
        assert menu_options.verify_maintenance_is_displaying_on_menu()
        assert menu_options.verify_claim_is_displaying_on_menu()
        assert menu_options.verify_buzz_is_displaying_on_menu()
        time.sleep(10)
