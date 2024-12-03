import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"checkBoxOption2").click()

driver.find_element(By.XPATH, "//input[@value='option3']").click()

assert driver.find_element(By.XPATH, "//input[@value='option3']").is_selected()

time.sleep(2)