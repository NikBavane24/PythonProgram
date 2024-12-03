import time

from selenium import webdriver
from selenium.webdriver.common.by import By
b = []
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
time.sleep(2)
fruits = driver.find_elements(By.XPATH,"//tr/td[1]")


for a in fruits :

    b.append(a.text)
c = b.copy()
b.sort()
print(b.sort())



assert b == c