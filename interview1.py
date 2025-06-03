import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Class:

    def Mobile(self,filter):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
        driver.find_element(By.XPATH,"//input[@placeholder='Search Brand']").send_keys(filter)
        driver.find_element(By.XPATH,"//div[@class='XqNaEv']").click()
        time.sleep(5)
c1=Class()
c1.Mobile("Apple")
