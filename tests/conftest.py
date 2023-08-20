import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as firefox_service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        service_obj = Service()
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser == "firefox":
        service_obj = firefox_service()
        options = firefox_options()
        driver = webdriver.Firefox(service=service_obj, options=options)
    driver.implicitly_wait(10)
    driver.get("http://ecoats-test.us-east-1.elasticbeanstalk.com/login")
    driver.maximize_window()

    request.cls.driver = driver
