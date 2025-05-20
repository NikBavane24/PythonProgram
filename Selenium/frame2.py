import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"(//div[@class='block large-row-spacer'])[5]")).perform()
time.sleep(2)
driver.switch_to.frame("courses-iframe")
text=driver.find_element(By.XPATH,"//span[@class='icon fa fa-envelope']/parent::*").text
print(text)
driver.switch_to.parent_frame()
action.send_keys(Keys.HOME).perform()
redio_button=driver.find_elements(By.XPATH,"//div[@id='radio-btn-example']/fieldset/label")
print(len(redio_button))
for i in redio_button:
    print(i.text)
    if i.text == "Radio3":
        i.click()
        break
        assert i.is_selected()

time.sleep(5)