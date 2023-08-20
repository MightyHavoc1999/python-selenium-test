from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CorporateProfilePage():

    def __init__(self, driver):
        self.driver = driver

    address2 = (By.CSS_SELECTOR, "input[placeholder='Enter Address2']")
    update_profile = (By.XPATH, "//button[text()='Update Profile']")
    new_department = (By.XPATH, "//button[text()='Add Department']")

    def update_address(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[placeholder='Enter Address2']")))
        self.driver.find_element(*CorporateProfilePage.address2).clear()
        self.driver.find_element(*CorporateProfilePage.address2).send_keys("APT 325")
        self.driver.find_element(*CorporateProfilePage.update_profile).click()

    def add_new_department(self):
        self.driver.find_element(*CorporateProfilePage.new_department).click()
        wait = WebDriverWait(self.driver, 10)
        modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "app-modal-host[class='ng-tns-c66-0']")))
        modal.find_element(By.XPATH, "//input[@name='deptName']").send_keys("Staples")
        modal.find_element(By.XPATH, "//input[@name='deptLocation']").send_keys("Boston")
        modal.find_element(By.XPATH, "//button[text()='Save']").click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Error']")))
        if modal.find_element(By.XPATH, "//span[text()='Error']").text == "Error":
            modal.find_element(By.XPATH, "//button[text()='CLOSE']").click()
            modal.find_element(By.XPATH, "//button[text()=' Cancel ']").click()

