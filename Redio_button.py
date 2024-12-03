import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='radio2']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@value='radio3']").click()

assert driver.find_element(By.XPATH, "//input[@value='radio3']").is_selected()

assert driver.find_element(By.XPATH, "//input[@value='radio3']").is_displayed()

time.sleep(2)