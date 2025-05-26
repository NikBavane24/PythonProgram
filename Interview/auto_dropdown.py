import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.ID,"APjFqb").send_keys("cricket score")
dropdown_atm=driver.find_elements(By.XPATH,"//li[@class='sbct PZPZlf']")

for i in dropdown_atm:
    print(i.text)
    if i.find_element(By.XPATH,"//div/span")=="cricket score":
        i.click()
time.sleep(5)