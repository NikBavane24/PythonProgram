

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="browser selection")

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()

    elif browser_name=="firefox":
        driver = webdriver.Firefox()


    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()





