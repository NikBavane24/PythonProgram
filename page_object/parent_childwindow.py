import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/mousemover/")
driver.find_element(By.LINK_TEXT,"DemoLink2").click()
window_open=driver.window_handles
print(window_open)
driver.switch_to.window(window_open[-1])
driver.find_element(By.ID,"APjFqb").send_keys("ABC")
driver.switch_to.window(window_open[0])

time.sleep(5)