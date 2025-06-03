import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/registration/")
driver.find_element(By.ID,"fname").send_keys("Shaurya")
driver.find_element(By.ID,"lname").send_keys("Bavane")
driver.find_element(By.NAME,"email").send_keys("shauryabavane@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Test@1234")
driver.find_element(By.XPATH,"//input[@id='male']").click()
dropdown = Select(driver.find_element('id','Skills'))
dropdown.select_by_visible_text("Technical Skills")
dropdown1 = Select(driver.find_element('id','Country'))
dropdown1.select_by_visible_text("India")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Present Address']").send_keys("Pune")
driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Permanent Address']").send_keys("Pune")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"button[name='Submit']")).perform()
driver.find_element(By.CSS_SELECTOR,"input[id='Pincode']").send_keys("411017")
dropdown3 = Select(driver.find_element('id','Relegion'))
dropdown3.select_by_visible_text("Hindu")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[id='file']")
driver.find_element(By.CSS_SELECTOR,"input[id='file']").send_keys("D:\\Resume\\Manual_API_Automation_Tester_Nikhil.pdf")
driver.find_element(By.CSS_SELECTOR,"input[id='relocate']").click()
time.sleep(5)