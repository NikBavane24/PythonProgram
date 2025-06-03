import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/flights/")
dropdown = Select(driver.find_element('name','From'))
dropdown.select_by_visible_text("GOI - Goa, IN")
dropdown1 = Select(driver.find_element('name','To'))
dropdown1.select_by_visible_text("BLR - Bangalore, IN")
driver.find_element(By.XPATH,"//input[@name='Departon']").send_keys("01-01-2025")
driver.find_element(By.XPATH,"//input[@name='Returnon']").send_keys("01-02-2025")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//input[@value='Search flights']")).perform()
time.sleep(1)
driver.find_element(By.XPATH,"//span[@title='2']").click()
driver.find_element(By.XPATH,"(//li[@role='treeitem'])[2]").click()
time.sleep(5)