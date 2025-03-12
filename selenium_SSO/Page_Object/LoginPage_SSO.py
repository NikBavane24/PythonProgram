from selenium.webdriver.common.by import By

from selenium_SSO.Page_Object.UsersPage_SSO import UsersPage


class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        #self.Continue_CesEmail=(By.XPATH,"//span[.='Continue with CES Email']")
        self.Email_address=(By.ID,"username")
        self.Password = (By.ID, "password")
        self.Continue_button=(By.XPATH,"//button[.='Continue']")
        self.otp = (By.ID, "code")
        self.Continue=(By.XPATH,"//button[.='Continue']")
        self.AdminPanel_button = (By.XPATH, "//span[.='Admin Panel']")





    def Login(self):
        #self.driver.find_element(* self.Continue_CesEmail).click()
        self.driver.find_element(*self.Email_address).send_keys("testmiq.qa@ces-ltd.com")
        self.driver.find_element(*self.Password).send_keys("Test@1234")
        self.driver.find_element(*self.Continue_button).click()
        self.driver.find_element(*self.otp).send_keys("377642")
        self.driver.find_element(*self.Continue).click()
        self.driver.find_element(*self.AdminPanel_button).click()




        users_page = UsersPage(self.driver)
        return users_page
