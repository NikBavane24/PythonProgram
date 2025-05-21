

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="Rahul"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
Alert=driver.switch_to.alert
Alert_text=Alert.text
time.sleep(5)
print(Alert_text)

assert Alert_text=="Hello Rahul, share this practice page and share your knowledge"
assert name in Alert_text
Alert.accept()




time.sleep(2)