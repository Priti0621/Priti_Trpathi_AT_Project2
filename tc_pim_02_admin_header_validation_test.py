import json
import time
import unittest
from selenium import webdriver
from AT_Project2.Page.tc_pim_02_admin_header_validation_page import ValidateTitleOfAdminPage
from orangehrmpages.login_page_class import HrmLoginPage


class TitleOfAdminPageTestClass(unittest.TestCase):
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
        title_of_admin_page = ValidateTitleOfAdminPage(cls.driver)
        title_of_admin_page.click_on_admin_menu()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # Tests case_ID  : TC_PIM_02 -Header validation on Admin page
    def test_header_validation_on_admin_page(self):
        title_of_admin_page = ValidateTitleOfAdminPage(self.driver)
        title_of_admin_page.verify_title_of_the_page()
        time.sleep(20)

    # Tests case_ID  : TC_PIM_02 - Options validation on Admin page
    #  Created object of admin header page and executed test case.
    def test_options_displaying_on_admin_page(self):
        title_of_admin_page = ValidateTitleOfAdminPage(self.driver)
        assert title_of_admin_page.verify_user_management_is_displaying()
        assert title_of_admin_page.verify_job_is_displaying()
        assert title_of_admin_page.verify_organization_is_displaying()
        assert title_of_admin_page.verify_qualifications_is_displaying()
        assert title_of_admin_page.verify_nationalities_is_displaying()
        assert title_of_admin_page.verify_corporate_banking_is_displaying()
        assert title_of_admin_page.verify_configuration_is_displaying()



