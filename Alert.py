import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "Nikhil"
driver.find_element(By.ID,"name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert

alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss()

