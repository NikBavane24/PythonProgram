from selenium.webdriver.common.by import By

from Selenium_FW_Testcase.page_Object.Checkout_Confirmation import Ckeckout_Confirmation
from Selenium_FW_Testcase.utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.shop_link=(By.XPATH, "//a[contains(@href,'shop')]")
        self.product_cards=(By.XPATH, "//div[@class='card h-100']")
        self.checkout_button=(By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()  # for CSS a[href*='shop']
        phones = self.driver.find_elements(*self.product_cards)

        for i in phones:
            phone_name = i.find_element(By.XPATH, "div/h4/a").text
            if phone_name == product_name:
                i.find_element(By.XPATH, "div/button").click()

    def gotoCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation=Ckeckout_Confirmation(self.driver)
        return checkout_confirmation



