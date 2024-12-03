
import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object.HomePage import HomePage
from utilities1.BASEclass1 import BaseClass


class TestHomePage(BaseClass):
    def __init__(self):
        self.driver = driver

    def test_formSubmission(self):

        time.sleep(3)
        homePage = HomePage(self.driver)
        homePage.getName().sendkeys("Nikhil")
        homePage.getEmail().sendkeys("nikhil@gmail.com")
        homePage.getPassword().send_keys("Ahbuvd@1234")
        homePage.getCheckbox().click()
        time.sleep(5)
        homePage.getRedio().click()
        homePage.getdataBinding().send_keys(" Hi")
        time.sleep(3)
        homePage.getBday().send_keys("24-02-2000")
        time.sleep(3)
        homePage.getSubmit().click()

