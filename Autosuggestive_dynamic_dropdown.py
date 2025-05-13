import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"autocomplete").send_keys("ind");
time.sleep(3)
country = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(len(country))
time.sleep(3)

for country1 in country:
    if country1.text == "India":
        country1.click()
        break
time.sleep(3)
print(driver.find_element(By.ID,"autocomplete").get_attribute("value"))

assert driver.find_element(By.ID,"autocomplete").get_attribute("value") == "India"