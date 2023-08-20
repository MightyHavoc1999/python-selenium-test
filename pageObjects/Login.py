from selenium.webdriver.common.by import By

from pageObjects.CorporateProfile import CorporateProfilePage


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "input[type='email']")
    password = (By.CSS_SELECTOR, "input[type='password']")
    submit = (By.CSS_SELECTOR, "button[class*='btn']")

    def login(self):
        self.driver.find_element(*LoginPage.username).send_keys("kvpankaj1999@gmail.com")
        self.driver.find_element(*LoginPage.password).send_keys("Pankaj@4b")
        self.driver.find_element(*LoginPage.submit).click()
        corporate_profile = CorporateProfilePage(self.driver)
        return corporate_profile

