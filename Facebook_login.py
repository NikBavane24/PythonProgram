import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.get("https://m.facebook.com/login/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("Abc@1234")
driver.find_element(By.NAME,"login").click()
msg = driver.find_element(By.XPATH,"//div[@class='_9ay7']").text
print(msg)
assert "The password that you've entered is incorrect." in msg
time.sleep(4)
driver.quit()
