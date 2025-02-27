import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Checkbox_element=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for i in Checkbox_element:
    if i.get_attribute("value")=="option2":
        i.click()
        assert  i.is_selected()
        break
time.sleep(2)

#Redio Button
Redio_button=driver.find_elements(By.CSS_SELECTOR,"input[class='radioButton']")
for i in Redio_button:
    if i.get_attribute("value")=="radio2":
        i.click()
        break
        assert i.is_selected()
time.sleep(2)
driver.find_element(By.ID,"hide-textbox").click()
driver.find_element(By.ID,"show-textbox").click()
assert driver.find_element(By.ID,"displayed-text").is_displayed()