import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from slenium_MIQ.page_object.cesGoldArchive_page import cesGoldArchive

class CreateReport:
    def __init__(self,driver):
        self.driver=driver
        self.clientsDropdown=(By.XPATH,"//input[@placeholder='Select Clients']")
        self.clientSelect=(By.XPATH,"(//span[.='Customized Energy Solutions'])[3]")
        self.clickOutside=(By.XPATH,"//label[.=' Clients ']")
        self.dropBox=(By.XPATH,"(//div[@class='k-upload-button-wrap']/input)[1]")
        self.highlights=(By.ID,"tinymce")
        self.publishReportButton=(By.XPATH,"//span[.='Publish Report']")
        self.noEmailPage = (By.XPATH, "//span[.='No']")

        self.SubtypeSearch = (By.CSS_SELECTOR, "input[placeholder='Select Sub-Types']")
        self.selectSubtypeSearch = (By.XPATH, "//span[.='Bulk System Planning']")
        self.topicSearch = (By.CSS_SELECTOR, "input[placeholder='Select Topics']")
        self.selectTopic = (By.XPATH, "(//li[@role='option'])[1]")
        self.selectTopic1 = (By.XPATH, "(//li[@role='option'])[2]")
        self.findSearch = (By.XPATH, "//span[.='Find Records']")

        self.selectReport=(By.CSS_SELECTOR,"div[row-id='0']")
        self.editReportButton = (By.XPATH, "//span[.='Edit Report']")
        self.titleReport=(By.CSS_SELECTOR,"input[placeholder='Enter Report Title']")


    def Report(self):
        time.sleep(2)
        self.driver.find_element(*self.clientsDropdown).click()
        self.driver.find_element(*self.clientSelect).click()
        self.driver.find_element(*self.clickOutside).click()
        file_input=self.driver.find_element(*self.dropBox)
        file_path="C:\\sample.pdf"
        file_input.send_keys(file_path)
        time.sleep(5)
        self.driver.switch_to.frame(0)
        self.driver.find_element(*self.highlights).send_keys("Test automated reports")
        self.driver.switch_to.default_content()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        self.driver.find_element(*self.publishReportButton).click()
        self.driver.find_element(*self.noEmailPage).click()

    def reportSearch(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/reports")
        self.driver.find_element(*self.SubtypeSearch).click()
        self.driver.find_element(*self.selectSubtypeSearch).click()
        self.driver.find_element(*self.topicSearch).click()
        self.driver.find_element(*self.selectTopic).click()
        self.driver.find_element(*self.selectTopic1).click()
        self.driver.find_element(*self.findSearch).click()

    def updateReport(self):
        self.driver.get("https://miq.qa.ces-ltd.com/admin/reports")
        self.driver.find_element(*self.selectReport).click()
        time.sleep(5)
        self.driver.find_element(*self.editReportButton).click()
        self.driver.find_element(*self.titleReport).send_keys("AESO Bulk and Regional Tariff Design Version2")
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        self.driver.find_element(*self.publishReportButton).click()
        self.driver.find_element(*self.noEmailPage).click()

        cesGoldArchive_page=cesGoldArchive(self.driver)
        return cesGoldArchive_page



