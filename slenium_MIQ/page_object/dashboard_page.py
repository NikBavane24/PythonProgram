from selenium.webdriver.common.by import By

from slenium_MIQ.page_object.createMeeting_page import CreateMeeting


class DashboardPage():
    def __init__(self,driver):
        self.driver=driver
        self.create_meeting=(By.XPATH,"//span[.='New Meeting']")



    def Dashboard(self):
        self.driver.find_element(*self.create_meeting).click()

        createMeeting_page=CreateMeeting(self.driver)
        return createMeeting_page

