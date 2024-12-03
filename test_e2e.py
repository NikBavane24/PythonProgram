import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.CheckOutPage import CheckOutPage
from page_object.ConfirmPage import ConfirmPage
from page_object.HomePage import HomePage
from page_object.final_Page import final_Page
from utilities1.BASEclass1 import BaseClass


#@pytest.mark.usefixtures("setup")

class Testone1(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    def test_e2e(self):

        homePage = HomePage(self.driver)

        self.driver.implicitly_wait(2)
        checkOutPage = HomePage.shopItems()
        # w_open = driver.window_handles
        # driver.switch_to.window(w_open[1])

        #checkOutPage = CheckOutPage(self.driver)

        orders = checkOutPage.getCardTitles()

        for order in orders:
            name = order.find_element(By.XPATH, "div/h4/a").text
            if name == "Blackberry":
                checkOutPage.getCardFooter().click()

        time.sleep(3)
        checkOutPage.checkOutItems().click()
        #self.time.sleep(3)
        ConfirmPage.getCheckOutButton().click()

       final_Page.FinalPage().send_keys("India")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        final_Page.passCountryName.click()
        final_Page.CheckBox().click()
        final_Page.Purchase().click()
        SuccessText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert ("Success! Thank you!" in SuccessText)
