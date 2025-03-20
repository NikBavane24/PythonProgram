import time
from selenium.webdriver.common.by import By


class MeetingTopic:
    def __init__(self,driver):
        self.driver=driver
        self.openMenu = (By.XPATH, "(//i[@class='icon icon-hamburger'])[2]")
        self.openMeetingTopicPage = (By.XPATH, "//a[@title='Meeting Topics']")
        self.addMeetingTopic=(By.XPATH,"//span[.='Add Meeting Topic']")
        self.topicName=(By.CSS_SELECTOR,"input[placeholder='Enter Topic']")
        self.topicDescription = (By.CSS_SELECTOR, "textarea[placeholder='Enter topic description here']")
        self.submitButton = (By.XPATH, "//span[.='Submit']")

        self.selectTopic = (By.CSS_SELECTOR, "div[row-id='0']")
        self.editTopicButton = (By.XPATH, "//span[.='Edit Details']")

        self.deleteTopic=(By.CSS_SELECTOR,"ces-button[title='Delete Topic']")
        self.confirmDelete=(By.XPATH,"//span[.='Confirm']")


    def createTopic(self):
        #self.driver.find_element(*self.openMenu).click()
        #self.driver.find_element(*self.openMeetingTopicPage).click()
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-topics")
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element(*self.addMeetingTopic).click()
        self.driver.find_element(*self.topicName).send_keys("New Topic")
        self.driver.find_element(*self.topicDescription).send_keys("Description for New Topic")
        time.sleep(2)
        self.driver.find_element(*self.submitButton).click()
        time.sleep(2)

    def updateTopic(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-topics")
        self.driver.find_element(*self.selectTopic).click()
        self.driver.find_element(*self.editTopicButton).click()
        self.driver.find_element(*self.topicName).send_keys(" update")
        self.driver.find_element(*self.topicDescription).send_keys(" update")
        time.sleep(2)
        self.driver.find_element(*self.submitButton).click()
        time.sleep(2)

    def TopicDelete(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-topics")
        time.sleep(2)
        self.driver.find_element(*self.selectTopic).click()
        self.driver.find_element(*self.deleteTopic).click()
        time.sleep(2)
        self.driver.find_element(*self.confirmDelete).click()


