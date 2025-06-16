import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):
    Ch = webdriver.ChromeOptions()
    Ch.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=Ch)
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    time.sleep(5)
    yield
    driver.close()

def test_example(setup):  # setup fixture is automatically called
    print("Running test")