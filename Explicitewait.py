import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
print(len(results))
count1 = len(results)
assert count1 > 0

for result in results:
    result.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
Sum = 0
for price in prices:
    Sum = Sum + int(price.text)

print(Sum)

total = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert Sum == total

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
#wait.until(expected_conditions.visibility_of_element_located(By.CSS_SELECTOR,".promoInfo"))
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
time.sleep(2)

distotal =float(driver.find_elements(By.CSS_SELECTOR,".discountAmt"))

assert  distotal < total