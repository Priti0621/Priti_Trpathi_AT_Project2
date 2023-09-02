from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainMenuValidation:
    def __init__(self, driver):
        self.menu_options_driver = driver

    # Locators of Menu available on left nav (side pan)

    admin_locator = "//span[text()='Admin']"
    pim_locator = "//span[text()='PIM']"
    leave_locator = "//span[text()='Leave']"
    time_locator = "//span[text()='Time']"
    recruitment_locator = "//span[text()='Recruitment']"
    my_info_locator = "//span[text()='My Info']"
    performance_locator = "//span[text()='Performance']"
    dashboard_locator = "//span[text()='Dashboard']"
    directory_locator = "//span[text()='Directory']"
    maintenance_locator = "//span[text()='Maintenance']"
    claim_locator = "//span[text()='Claim']"
    buzz_locator = "//span[text()='Buzz']"

    def verify_admin_is_displaying_on_menu(self):
        admin_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.admin_locator)))
        return admin_options

    def verify_pim_is_displaying_on_menu(self):
        pim_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.pim_locator)))
        return pim_options

    def verify_leave_is_displaying_on_menu(self):
        leave_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.leave_locator)))
        return leave_options

    def verify_time_is_displaying_on_menu(self):
        time_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.time_locator)))
        return time_options

    def verify_recruitment_is_displaying_on_menu(self):
        recruitment_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.recruitment_locator)))
        return recruitment_options

    def verify_my_info_is_displaying_on_menu(self):
        my_info_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.my_info_locator)))
        return my_info_options

    def verify_performance_is_displaying_on_menu(self):
        performance_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.performance_locator)))
        return performance_options

    def verify_dashboard_is_displaying_on_menu(self):
        dashboard_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.dashboard_locator)))
        return dashboard_options

    def verify_directory_is_displaying_on_menu(self):
        directory_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.directory_locator)))
        return directory_options

    def verify_maintenance_is_displaying_on_menu(self):
        maintenance_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.maintenance_locator)))
        return maintenance_options

    def verify_claim_is_displaying_on_menu(self):
        claim_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.claim_locator)))
        return claim_options

    def verify_buzz_is_displaying_on_menu(self):
        buzz_options = WebDriverWait(self.menu_options_driver, 5).until(EC.presence_of_element_located((By.XPATH, self.buzz_locator)))
        return buzz_options








