import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#river = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.ID,"APjFqb").send_keys("India")
time.sleep(4)
Title=driver.title
print(Title)

Url=driver.current_url
print(Url)

driver.quit()