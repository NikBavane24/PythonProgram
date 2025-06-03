import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/multi-level-dropdown/")
dropdown1= Select(driver.find_element("id","outer-dropdown"))
dropdown1.select_by_visible_text("Drop3")
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.element_to_be_clickable((By.ID, "inner-dropdown")))
dropdown2= Select(driver.find_element("id","inner-dropdown"))
dropdown2.select_by_visible_text("Option2")
time.sleep(5)