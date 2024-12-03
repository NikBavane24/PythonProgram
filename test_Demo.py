
import pytest
import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    #def __init__(self):
        #self.driver = None

    def test_Demo(self,setup):


        setup.driver.implicitly_wait(5)
        setup.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
        time.sleep(2)
        results = setup.driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
        print(len(results))
        count1 = len(results)
        assert count1 > 0

        for result in results:
            result.click()

        setup.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
        setup.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        # time.sleep(2)
        setup.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
        setup.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        # time.sleep(5)
        print(setup.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
        time.sleep(2)
