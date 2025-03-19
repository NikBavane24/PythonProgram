import time
from selenium.webdriver.common.by import By
from slenium_MIQ.page_object.createReport_page import CreateReport

class CreateMeeting:
    def __init__(self,driver):
        self.driver=driver
        self.toggleCalendar=(By.XPATH,"(//button[@title='Toggle calendar'])[1]")
        self.today_meetingDate=(By.XPATH,"(//span[.=' Today '])[2]")
        self.market=(By.XPATH,"(//span[@class='k-input-value-text'])[2]")
        self.selectMarket=(By.XPATH,"(//li[@role='option'])[1]")
        self.meetingType = (By.XPATH, "(//span[@class='k-input-value-text'])[3]")
        self.selectMeetingType = (By.XPATH, "(//li[@role='option'])[3]")
        self.subType = (By.XPATH, "(//span[@class='k-input-value-text'])[4]")
        self.selectSubType = (By.XPATH, "(//li[@role='option'])[1]")
        self.selectSubType1 = (By.XPATH, "(//li[@role='option'])[2]")
        self.topic=(By.XPATH,"(//input[@role='combobox'])[3]")
        self.selectTopic = (By.XPATH, "(//li[@role='option'])[1]")
        self.selectTopic1 = (By.XPATH, "(//li[@role='option'])[2]")
        self.clickOutside=(By.XPATH,"//kendo-label")
        self.submitButton=(By.XPATH,"//span[.='Submit']")

        self.SubtypeSearch = (By.CSS_SELECTOR, "input[placeholder='Select Sub-Types']")
        self.topicSearch = (By.CSS_SELECTOR, "input[placeholder='Select Topics']")
        self.findSearch = (By.XPATH, "//span[.='Find Records']")

        self.selectMeeting=(By.XPATH,"//div[@row-id='0']")
        self.editButton=(By.XPATH,"//span[.='Edit Details']")
        self.description = (By.XPATH, "(//input[@class='k-input-inner'])[4]")

        self.deleteMeeting = (By.XPATH, "(//button[@type='button'])[8]")
        self.confirmButton = (By.XPATH, "//span[.='Confirm']")



    def Meeting(self):
        self.driver.find_element(*self.toggleCalendar).click()
        self.driver.find_element(*self.today_meetingDate).click()
        self.driver.find_element(*self.market).click()
        self.driver.find_element(*self.selectMarket).click()
        self.driver.find_element(*self.meetingType).click()
        self.driver.find_element(* self.selectMeetingType).click()
        self.driver.find_element(*self.subType).click()
        self.driver.find_element(*self.selectSubType).click()
        self.driver.find_element(*self.topic).click()
        self.driver.find_element(*self.selectTopic).click()
        self.driver.find_element(*self.clickOutside).click()
        self.driver.find_element(*self.submitButton).click()
        time.sleep(2)
        current_url = self.driver.current_url
        print("Current URL:", current_url)

        report_page=CreateReport(self.driver)
        return report_page

    def meetingSearch(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meetings")
        self.driver.find_element(*self.SubtypeSearch).click()
        self.driver.find_element(* self.selectSubType).click()
        self.driver.find_element(*self.topicSearch).click()
        self.driver.find_element(*self.selectTopic).click()
        self.driver.find_element(*self.findSearch).click()


    def updateMeeting(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meetings")
        self.driver.find_element(*self.selectMeeting).click()
        self.driver.find_element(*self.editButton).click()
        time.sleep(1)
        self.driver.find_element(*self.subType).click()
        self.driver.find_element(*self.selectSubType1).click()
        self.driver.find_element(*self.topic).click()
        #self.driver.find_element(*self.selectTopic).click()
        self.driver.find_element(*self.selectTopic1).click()
        self.driver.find_element(*self.clickOutside).click()
        self.driver.find_element(*self.description).send_keys("Updated")
        self.driver.find_element(*self.submitButton).click()

    def deleteMeeting(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meetings")
        self.driver.find_element(*self.selectMeeting).click()
        self.driver.find_element(*self.deleteMeeting).click()
        self.driver.find_element(*self.confirmButton).click()




