from selenium.webdriver.common.by import By

from slenium_MIQ.page_object.meetingTypes_page import MeetingTypes


class cesGoldArchive:
    def __init__(self,driver):
        self.driver=driver
        self.market=(By.CSS_SELECTOR,"input[placeholder='Select Market']")
        self.selectMarket=(By.XPATH,"(//li[@role='option'])[1]")
        self.subType = (By.CSS_SELECTOR, "input[placeholder='Select Sub-Types']")
        self.selectSubtype = (By.XPATH, "(//li[@role='option'])[1]")
        self.client = (By.CSS_SELECTOR, "input[placeholder='Select Clients']")
        self.selectClient = (By.XPATH, "(//li[@role='option'])[37]")
        self.findSearch = (By.XPATH, "//span[.='Find Records']")


    def goldArchiveReportSearch(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/ces-gold-archive")
        self.driver.find_element(*self.market).click()
        self.driver.find_element(*self.selectMarket).click()
        self.driver.find_element(* self.subType).click()
        self.driver.find_element(* self.selectSubtype).click()
        self.driver.find_element(*self.client).click()
        self.driver.find_element(*self.selectClient).click()
        self.driver.find_element(*self.findSearch).click()

        meetingTypes_page = MeetingTypes(self.driver)
        return meetingTypes_page