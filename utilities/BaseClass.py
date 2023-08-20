import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def select_options_by_text(locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def check_if_tabs_open(self):
        tabs = self.driver.find_elements(By.XPATH, "//ul[@id='collapseBasic']")

        if tabs[0].get_attribute("class") == "collapse":
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Administration']")))
            self.driver.find_element(By.XPATH, "//span[text()='Administration']").click()
        if tabs[1].get_attribute("class") == "collapse":
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Employee Services']")))
            self.driver.find_element(By.XPATH, "//span[text()='Employee Services']").click()
