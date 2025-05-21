import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Click Here").click()
window_open=driver.window_handles
print(window_open)

driver.switch_to.window(window_open[-1])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "New Window"==driver.find_element(By.TAG_NAME,"h3").text
time.sleep(2)
driver.close()

driver.switch_to.window(window_open[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window"==driver.find_element(By.TAG_NAME,"h3").text
time.sleep(2)