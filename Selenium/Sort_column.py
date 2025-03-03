import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browsersorted=[]
driver.implicitly_wait(5)
time.sleep(1)
driver.find_element(By.XPATH,"//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
sort_list=driver.find_elements(By.XPATH,"//tr/td[1]")
for i in sort_list:
    browsersorted.append(i.text)

Actualsorted=browsersorted.copy()
time.sleep(3)
print(browsersorted)

browsersorted.sort()
print(Actualsorted)

assert Actualsorted==browsersorted