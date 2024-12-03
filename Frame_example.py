import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']").click()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
#print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.find_element(By.XPATH,"//body[@id='tinymce']").clear()
driver.find_element(By.XPATH,"//body[@id='tinymce']").send_keys("I am automate frame")
time.sleep(2)

driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@value='option2']")
time.sleep(2)