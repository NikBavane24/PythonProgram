import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#river = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("Test@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Test@1234")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


time.sleep(4)
