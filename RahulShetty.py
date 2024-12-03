
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("qwerty")
driver.find_element(By.NAME,"email").send_keys("qwer@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Ahbuvd@1234")
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys(" Hi")
driver.find_element(By.XPATH,"(//input[@name='bday'])").send_keys("24-02-2000")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='submit'])").click()
time.sleep(3)


# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute='value']-> input[type='submit'], #id, .classname
