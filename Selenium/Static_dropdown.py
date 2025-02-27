import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#river = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"name").send_keys("abcdef")
driver.find_element(By.NAME,"email").send_keys("abcd@email.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("abc@1234")
driver.find_element(By.ID,"exampleCheck1").click()

#Static dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
Text_msg=driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
print(Text_msg)
assert "Success! The Form has been submitted successfully!." in Text_msg

time.sleep(4)