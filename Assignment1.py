import time

import countries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
Next_page = driver.window_handles
driver.switch_to.window(Next_page[1])
a = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print(a)
driver.switch_to.window(Next_page[0])
driver.find_element(By.ID,"username").send_keys(a)
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Test@1234")
driver.find_element(By.XPATH,"(//span[@class='checkmark'])[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//button)[2]").click()
driver.find_element(By.XPATH,"//select").click()
driver.find_element(By.XPATH,"(//div/select/option)[2]").click()
driver.find_element(By.ID,"terms").click()
time.sleep(3)
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)