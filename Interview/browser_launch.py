import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("India")
Title=driver.title
print(Title)
driver.find_element(By.LINK_TEXT,"Gmail").click()
Title=driver.title
print(Title)
driver.back()
Title=driver.title
print(Title)
driver.refresh()
driver.forward()
#driver.find_element(By.XPATH,"(//input[@value='Google Search'])[2]").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
