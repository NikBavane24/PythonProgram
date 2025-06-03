import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/hoverable-dropdown/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"button[class='dropbtn']")).perform()
driver.find_element(By.XPATH,"//span[text()='Drop1']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//li[text()='Drop2']").click()
time.sleep(1)
time.sleep(5)