from selenium.webdriver.common.by import By
from slenium_MIQ.page_object.createMeeting_page import CreateMeeting

class DashboardPage():
    def __init__(self,driver):
        self.driver=driver
        self.create_meeting=(By.XPATH,"//span[.='New Meeting']")
        self.searchField=(By.XPATH,"//input[@type='text']")
        self.todayMeetings = (By.XPATH, "//td[@class='k-scheduler-cell todayMeeting k-selected meetingDate']")



    def Dashboard(self):
        self.driver.find_element(*self.create_meeting).click()

        createMeeting_page=CreateMeeting(self.driver)
        return createMeeting_page

    def report_search(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/dashboard")
        self.driver.find_element(*self.searchField).send_keys("AESO")
        ISO=self.driver.find_elements(By.XPATH,'//span[@class="highlighted-text"]/span/span/span/span')

        for i in ISO:
            if ISO=="AESO":
                pass
            else:
                print("Search field not available")

        self.driver.find_element(*self.todayMeetings).click()
        meetings=self.driver.find_elements(By.XPATH,"//div[@class='meeting-list-item']")
        noofMeeting=len(meetings)
        assert noofMeeting>0





