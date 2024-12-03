import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    Ch = webdriver.ChromeOptions()
    Ch.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=Ch)
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
