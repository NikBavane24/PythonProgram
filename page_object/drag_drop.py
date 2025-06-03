import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/drag-and-drop/")
action = ActionChains(driver)
source = driver.find_element(By.XPATH,"//img[@id='drag6']")
target = driver.find_element(By.XPATH,"//div[@id='div2']")
action.drag_and_drop(source,target).perform()
time.sleep(5)