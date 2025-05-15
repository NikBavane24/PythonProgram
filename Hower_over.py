import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action=ActionChains(driver)

#WebElement e1= driver.find_element(By.ID,"mousehover")
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(3)
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
#time.sleep(3)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(3)

action.double_click(driver.find_element(By.ID,"checkBoxOption2")).perform()
time.sleep(3)