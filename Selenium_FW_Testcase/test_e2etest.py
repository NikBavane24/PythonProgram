import json
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_FW_Testcase.page_Object.Login_Page import LoginPage
from Selenium_FW_Testcase.page_Object.ShopPage import ShopPage
test_data_path='data/test_e2etest.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver=browserInstance

    loginPage=LoginPage(driver)
    print(loginPage.getTitle())
    shop_page=loginPage.Login(test_list_item["userEmail"],test_list_item["userPassword"])

    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout_confirmation=shop_page.gotoCart()
    print(checkout_confirmation.getTitle())
    time.sleep(2)
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ind")
    checkout_confirmation.validate_order()

    time.sleep(2)
