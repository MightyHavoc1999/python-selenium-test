from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass
from pageObjects.Login import LoginPage
from pageObjects.Clients import ClientsPage


class TestE2E(BaseClass):
    clients_tab = (By.XPATH, "//a[@href='/pages/clients']")
    profile_tab = (By.XPATH, "//a[@href='/pages/my-profile']")
    projects_tab = (By.XPATH, "//a[@href='/pages/projects']")
    employees_tab = (By.XPATH, "//a[@href='/pages/employees']")
    timesheets_tab = (By.XPATH, "//a[@href='/pages/timesheets/timesheets']")
    reports_tab = (By.XPATH, "//a[@href='/pages/reports']")
    charge_codes_tab = (By.XPATH, "//a[@href='/pages/charge-codes']")
    appraisal_goals_tab = (By.XPATH, "//a[@href='/pages/appraisal/set-appraisal-goals']")
    appraisal_feedback_tab = (By.XPATH, "//a[@href='/pages/appraisal/submit-appraisal']")


    def test_e2e(self):
        logger = self.get_logger()
        logger.info("Starting the Testing from Login to Logout")
        logger.info("On the Login Page")
        login_page = LoginPage(self.driver)

        corporate_page = login_page.login()
        corporate_page.update_address()
        corporate_page.add_new_department()

        self.check_if_tabs_open()

        clients_page = ClientsPage(self.driver, TestE2E.select_options_by_text)

        self.driver.find_element(*TestE2E.clients_tab).click()

        ClientsPage.add_client(clients_page, self.driver)

        self.check_if_tabs_open()

        self.driver.find_element(*TestE2E.projects_tab).click()
        self.driver.find_element(*TestE2E.employees_tab).click()
        self.driver.find_element(*TestE2E.timesheets_tab).click()
        self.driver.find_element(*TestE2E.reports_tab).click()
        self.driver.find_element(*TestE2E.charge_codes_tab).click()
        self.driver.find_element(*TestE2E.profile_tab).click()
        self.driver.find_element(*TestE2E.appraisal_goals_tab).click()
        self.driver.find_element(*TestE2E.appraisal_feedback_tab).click()

        elements = self.driver.find_elements(By.CSS_SELECTOR, "a[role='button']")
        elements[2].click()
        self.driver.find_element(By.XPATH, "//a[text()=' Sign out']").click()








