import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#river = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").send_keys("ind")
time.sleep(1)
dropdown_elements=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(len(dropdown_elements))
for i in dropdown_elements:
    if i.text=="India":
        i.click()
        break

#print(driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").text)
print(driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").get_attribute("value"))
assert driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").get_attribute("value")=="India"

time.sleep(1)