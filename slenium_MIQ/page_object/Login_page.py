import time
from selenium.webdriver.common.by import By
from slenium_MIQ.page_object.dashboard_page import DashboardPage
from slenium_MIQ.page_object.meetingTypes_page import MeetingTypes
from slenium_MIQ.page_object.topic_page import MeetingTopic

class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.userEmail=(By.ID,"username")
        self.userPassword = (By.ID, "password")
        self.continueButton = (By.XPATH,"//button[@value='default']")
        self.otp=(By.ID,"code")
        self.continueButton1 = (By.XPATH, "//button[.='Continue']")

    def Login(self):
        self.driver.find_element(*self.userEmail).send_keys("testmiq.qa@ces-ltd.com")
        self.driver.find_element(*self.userPassword).send_keys("Test@1234")
        self.driver.find_element(*self.continueButton).click()
        self.driver.find_element(*self.otp).send_keys("099881")
        self.driver.find_element(*self.continueButton1).click()


        dashboard_page=DashboardPage(self.driver)
        return dashboard_page
        time.sleep(5)

