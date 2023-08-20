from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientsPage:
    def __init__(self, driver, selector):
        self.driver = driver
        self.selector = selector

    add_client_button = (By.XPATH, "//button[text()='Add Client']")

    @staticmethod
    def add_client(client_obj, driver):
        driver.find_element(*ClientsPage.add_client_button).click()
        wait = WebDriverWait(driver, 20)
        modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "app-modal-host[class='ng-tns-c66-0']")))
        modal.find_element(By.CSS_SELECTOR, "input[name='clientName']").send_keys("Test")
        modal.find_element(By.CSS_SELECTOR, "input[name='clientAddress1']").send_keys("Test")
        modal.find_element(By.CSS_SELECTOR, "input[name='clientAddress1']").send_keys("Test")
        select_locator = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
        client_obj.selector(select_locator, "United States")
        select_locator = driver.find_element(By.CSS_SELECTOR, "select[name='state']")
        client_obj.selector(select_locator, "Virginia")
        modal.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Test")
        modal.find_element(By.CSS_SELECTOR, "input[name='zip']").send_keys("12345")
        modal.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("1234567890")
        modal.find_element(By.XPATH, "//button[text()='Save']").click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Error']")))
        if modal.find_element(By.XPATH, "//span[text()='Error']").text == "Error":
            modal.find_element(By.XPATH, "//button[text()='CLOSE']").click()
            modal.find_element(By.XPATH, "//button[text()=' Cancel ']").click()

