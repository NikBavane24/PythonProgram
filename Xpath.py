import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/otp?wizard_id=ThP2NhSPmml9ijtQTiVn3JERbnFtOTZNHygw2SaUGukuIsPdBGW4MqVC61110D7JhPsYG-j_egImNSOlHBZMcw")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abc")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("acdnuidb@gmail.com")
driver.find_element(By.XPATH,"//input[@id='allowMarketingEmails']").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"input[type='button']").click()


time.sleep(4)