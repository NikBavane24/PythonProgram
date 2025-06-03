import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/alert/")
driver.find_element(By.XPATH,"(//button[.='Alert1'])[1]").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
driver.find_element(By.XPATH,"(//button[.='Received1'])[1]").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(5)