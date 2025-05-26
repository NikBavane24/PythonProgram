import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Shaurya")
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("shaurya@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder = 'Password']").send_keys("Test@1234")
driver.find_element(By.XPATH,"//input[@id= 'exampleCheck1']").click()
dropdown_gender = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown_gender.select_by_visible_text("Male")
driver.find_element(By.ID,"inlineRadio1").click()
driver.find_element(By.NAME,"bday").send_keys("05-07-2021")
time.sleep(5)