from selenium import webdriver
from selenium.webdriver.common.by import By


def method(self):
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("")
    driver.find_element(By.ID,"")
    element =driver.find_elements(By.CLASS_NAME,"")
    for i in element:
        if element.text=="":
            assert True