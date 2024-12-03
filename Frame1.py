import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.switch_to.frame("courses-iframe")

driver.find_element(By.LINK_TEXT,"Mentorship").click()
time.sleep(3)