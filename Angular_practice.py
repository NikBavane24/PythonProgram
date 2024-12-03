import time

from django.contrib.messages import success
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

Ch = webdriver.ChromeOptions()
Ch.add_argument("--start-maximized")
driver = webdriver.Chrome(options=Ch)
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
#w_open = driver.window_handles
#driver.switch_to.window(w_open[1])

orders = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for order in orders:
    name = order.find_element(By.XPATH,"div/h4/a").text
    if name == "Blackberry":
        order.find_element(By.XPATH,"div/button").click()

time.sleep(3)
driver.find_element(By.XPATH,"(//li/a)[3]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//td/button)[3]").click()

driver.find_element(By.XPATH,"//input[@id='country']").send_keys("India")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
SuccessText = driver.find_element(By.CLASS_NAME,"alert-success").text

assert ("Success! Thank you!" in SuccessText)