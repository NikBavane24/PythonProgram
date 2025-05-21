import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(2)
window=driver.window_handles

driver.switch_to.window(window[-1])
Email=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print(Email)
time.sleep(2)
driver.switch_to.window(window[0])
time.sleep(2)
driver.find_element(By.ID,"username").send_keys(Email)
driver.find_element(By.ID,"password").send_keys("Test@1234")
driver.find_element(By.XPATH,"(//span[@class='checkmark'])[2]").click()
dropdown=Select(driver.find_element(By.XPATH,"//select"))
dropdown.select_by_value("teach")
#driver.find_element(By.ID,'terms').click()
driver.find_element(By.XPATH,"//button[@id='okayBtn']").click()
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()
time.sleep(20)