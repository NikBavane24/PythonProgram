import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/scrolling/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Age")).perform()
time.sleep(5)
driver.close()