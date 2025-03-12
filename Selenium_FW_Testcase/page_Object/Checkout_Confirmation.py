from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_FW_Testcase.utils.browserutils import BrowserUtils


class Ckeckout_Confirmation(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.country_input=(By.ID, "country")
        self.country_option=(By.LINK_TEXT, "India")
        self.checkbox=(By.CSS_SELECTOR, "label[for='checkbox2']")
        self.submitButton =(By.CSS_SELECTOR, "input[value='Purchase']")
        self.success_message=(By.CSS_SELECTOR, "div[class*='alert']")




    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()



    def enter_delivery_address(self,countryname):
        self.driver.find_element(*self.country_input).send_keys(countryname)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submitButton).click()




    def validate_order(self):
        Msg = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in Msg
