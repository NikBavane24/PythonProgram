import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/add-to-cart/")
driver.switch_to.frame("frame")
driver.find_element(By.ID,"firstName").send_keys("ABC")
driver.find_element(By.NAME,"lastName").send_keys("Test@1234")
time.sleep(5)