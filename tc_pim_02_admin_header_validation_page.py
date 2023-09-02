from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ValidateTitleOfAdminPage:

    # Constructor of the page.
    def __init__(self, driver):
        self.adminpage_driver = driver

    #Locators of Admin page

    admin_menu_locator = "//span[text()='Admin']"
    title_page_locator = "//span[@class='oxd-topbar-header-breadcrumb']"
    user_management_locator = "//span[contains(text(),'User Management ')]/.."
    job_locator = "//span[text()='Job ']"
    organization_locator = "//span[text()='Organization ']"
    qualifications_locator = "//span[text()='Qualifications ']"
    nationalities_locator = "//a[text()='Nationalities']"
    corporate_banking_locator = "//a[text()='Corporate Branding']"
    configuration_locator = "//span[text()='Configuration ']"

    # created methods to call above locators and perform actions.
    # click on Admin in menu(side pane)
    def click_on_admin_menu(self):
        self.adminpage_driver.find_element(By.XPATH, self.admin_menu_locator).click()

    # this is to check title of the Admin page.
    def verify_title_of_the_page(self):
        self.adminpage_driver.find_element(By.XPATH, self.title_page_locator)

    # Below all methods are created for options displaying on Admin page.

    def verify_user_management_is_displaying(self):
        user_management_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                           self.user_management_locator)))
        return user_management_present

    def verify_job_is_displaying(self):
        job_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH, self.job_locator)))
        return job_present

    def verify_organization_is_displaying(self):
        organization_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                            self.organization_locator)))
        return organization_present

    def verify_qualifications_is_displaying(self):
        qualifications_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                            self.qualifications_locator)))
        return qualifications_present


    def verify_nationalities_is_displaying(self):
        nationalities_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                            self.nationalities_locator)))
        return nationalities_present

    def verify_corporate_banking_is_displaying(self):
       corporate_banking_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                            self.corporate_banking_locator)))
       return corporate_banking_present

    def verify_configuration_is_displaying(self):
        configuration_present = WebDriverWait(self.adminpage_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                            self.configuration_locator)))
        return configuration_present






