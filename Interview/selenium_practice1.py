import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    product_name=product.find_element(By.XPATH,"div/h4/a").text
    #print(product_name)
    if product_name=="Nokia Edge":
        print("product_name=",product_name)
        driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[3]").click()
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
    #driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

time.sleep(5)