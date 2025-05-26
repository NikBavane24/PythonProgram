import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.find_element(By.LINK_TEXT,"Mobiles").click()
No_of_links=driver.find_elements(By.XPATH,"//a")
print(len(No_of_links))
for link in No_of_links:
    href=link.get_attribute("href")
    print(href)
time.sleep(5)