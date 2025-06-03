import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/dropdown/")
driver.find_element(By.XPATH,"(//span[@title='Select Choice 1'])[1]").click()
#dropdown = Select(driver.find_element(By.CLASS_NAME,"form-select Choice1 select2-hidden-accessible"))
element=driver.find_element(By.XPATH,"//input[@class='select2-search__field']")
element.send_keys("Demo1")
element.send_keys(Keys.ENTER)
#driver.find_element(By.XPATH,"(//span[@title='Select Choice 5'])[1]").click()
dropdown = Select(driver.find_element(By.ID,"Choice5"))
dropdown.select_by_value("Day5")
time.sleep(5)
