import time
from selenium.webdriver.common.by import By


class UsersPage():
    def __init__(self,driver):
        self.driver=driver
        self.usersPage=(By.XPATH,'//a[@title="Users"]')
        self.addNewUser = (By.XPATH, '//span[.="Add New User"]')
        self.FirstName = (By.XPATH,"//input[@id='firstname']")
        self.LastName = (By.XPATH,"//input[@id='lastname']")
        self.Email = (By.XPATH,"//input[@id='emailId']")
        self.Password=(By.XPATH,"//input[@id='passwordId']")
        self.RepeatPassword = (By.XPATH, "//input[@id='repeatPasswordId']")
        self.Continue_button = (By.XPATH, "//span[.='Continue']")
        self.select_application = (By.XPATH, "(//span[.='MarketIQ'])[2]")
        self.organization=(By.XPATH,"//span[@id='k-34cd329e-e069-4a97-a374-63fc34383dd0']")

        #self.search=(By.XPATH,"//input[@id='null']")



    def Users(self):
        self.driver.find_element(*self.usersPage).click()
        self.driver.find_element(*self.addNewUser).click()
        time.sleep(2)
        self.driver.find_element(*self.FirstName).send_keys("Rahul")
        self.driver.find_element(*self.LastName).send_keys("More")
        self.driver.find_element(*self.Email).send_keys("rahulmore@gmial.com")
        self.driver.find_element(*self.Password).send_keys("Test@1234")
        self.driver.find_element(*self.RepeatPassword).send_keys("Test@1234")
        self.driver.find_element(*self.Continue_button).click()
        self.driver.find_element(*self.select_application).click()
        self.driver.find_element(*self.Continue_button).click()
        time.sleep(2)
        self.driver.find_element(*self.organization).click()


    #def Delete(self):
        #self.driver.find_element(*self.search).send_keys("More")



