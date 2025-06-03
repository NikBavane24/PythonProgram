import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/rightclick/")
action = ActionChains(driver)
action.context_click(driver.find_element(By.XPATH,"//a[.='Practice Link1']")).perform()
time.sleep(5)