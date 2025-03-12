from selenium.webdriver.common.by import By


class CreateMeeting:
    def __init__(self,driver):
        self.driver=driver
        self.toggleCalendar=(By.XPATH,"(//button[@title='Toggle calendar'])[1]")
        self.market_dropdown=(By.XPATH,"(//span[@class='k-input-value-text'])[2]")



    def Meeting(self):
        self.driver.find_element(*self.toggleCalendar).click()
        self.driver.find_element(*self.market_dropdown).click()


