import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#river = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
fruit_name="Banana"
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
price=driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-4-undefined']").text
print(price)



time.sleep(5)