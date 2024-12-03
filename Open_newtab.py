import time

import countries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(3)

window_open = driver.window_handles
driver.switch_to.window(window_open[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "New Window" ==driver.find_element(By.TAG_NAME,"h3").text

driver.close()

driver.switch_to.window(window_open[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

assert "Opening a new window" ==driver.find_element(By.TAG_NAME,"h3").text