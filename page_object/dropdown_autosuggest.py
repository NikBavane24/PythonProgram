import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("Ind")
dropdown_elements= driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for dropdown_element in dropdown_elements:
    if dropdown_element.text=="India":
        dropdown_element.click()
driver.close()

time.sleep(5)