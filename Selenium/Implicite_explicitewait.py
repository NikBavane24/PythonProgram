import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ca")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
#print(count)
assert count>0


for i in results:
    i.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[.='PROCEED TO CHECKOUT']").click()
#time.sleep(2)

driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
Wait=WebDriverWait(driver,10)
Wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#time.sleep(8)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)


time.sleep(2)