from selenium.webdriver.common.by import By

from Selenium_FW_Testcase.page_Object.ShopPage import ShopPage
from Selenium_FW_Testcase.utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.checkbox=(By.ID, "terms")
        self.signin=(By.ID, "signInBtn")


    def Login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.signin).click()
        shop_page = ShopPage(self.driver)
        return shop_page