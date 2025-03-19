import time
from selenium.webdriver.common.by import By


class MeetingTypes:
    def __init__(self,driver):
        self.driver=driver
        self.openMenu=(By.XPATH,"(//i[@class='icon icon-hamburger'])[2]")
        self.openMeetingTypePage=(By.XPATH,"//a[@title='Meeting Types']")
        self.addMeetingTypeButton=(By.XPATH,"//span[.='Add Meeting Type']")
        self.Market = (By.XPATH, "(//span[.='Select Market'])[2]")
        self.selectMarket = (By.XPATH, "(//li[@role='option'])[1]")
        self.typeName = (By.CSS_SELECTOR, "input[placeholder='Enter type name']")
        self.description = (By.CSS_SELECTOR, "textarea[placeholder='Meeting type description here']")
        self.submitButton = (By.XPATH, "//span[.='Submit']")

        self.addMeetingSubtypeButton = (By.XPATH, "//span[.='Add Meeting Sub Type']")
        self.subTypeName = (By.CSS_SELECTOR, "input[placeholder='Enter meeting sub-type name']")
        self.SubTypeDescription = (By.CSS_SELECTOR, "textarea[placeholder='Meeting sub type description']")

        self.selectMeetingType = (By.CSS_SELECTOR, "div[row-id='0']")
        self.editMeetingTypeButton = (By.XPATH, "//span[.='Edit Meeting Type']")

        self.selectMeetingSubType = (By.CSS_SELECTOR, "div[row-id='0']")
        self.editMeetingSubTypeButton = (By.XPATH, "//span[.='Edit Details']")


    def createMeetingType(self):
        self.driver.find_element(*self.openMenu).click()
        time.sleep(2)
        self.driver.find_element(*self.openMeetingTypePage).click()
        #self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-types")
        self.driver.find_element(*self.addMeetingTypeButton).click()
        self.driver.find_element(*self.Market).click()
        self.driver.find_element(*self.selectMarket).click()
        self.driver.find_element(*self.typeName).send_keys("AESO Type")
        self.driver.find_element(*self.description).send_keys("AESO Type Description")
        self.driver.find_element(*self.submitButton).click()

    def createMeetingSubtype(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-types")
        self.driver.find_element(*self.selectMeetingType).click()
        time.sleep(2)
        self.driver.find_element(*self.addMeetingSubtypeButton).click()
        time.sleep(2)
        self.driver.find_element(*self.subTypeName).send_keys("AESO SubType")
        time.sleep(2)
        self.driver.find_element(*self.SubTypeDescription).send_keys("AESO SubType Description")
        time.sleep(2)
        self.driver.find_element(*self.submitButton).click()
        time.sleep(2)


    def updateMeetingType(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-types")
        self.driver.find_element(*self.selectMeetingType).click()
        self.driver.find_element(*self.editMeetingTypeButton).click()
        self.driver.find_element(*self.typeName).send_keys(" Updated")
        self.driver.find_element(*self.description).send_keys(" Updated")
        self.driver.find_element(*self.submitButton).click()
        time.sleep(2)

    def updateMeetingSubType(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/meeting-types")
        self.driver.find_element(*self.selectMeetingType).click()
        time.sleep(2)
        self.driver.find_element(*self.selectMeetingSubType).click()
        self.driver.find_element(*self.editMeetingSubTypeButton).click()
        self.driver.find_element(*self.subTypeName).send_keys(" Update")
        self.driver.find_element(*self.SubTypeDescription).send_keys(" Update")
        self.driver.find_element(*self.submitButton).click()
