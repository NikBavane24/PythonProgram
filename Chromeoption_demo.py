import time
from turtledemo.penrose import start

from selenium import webdriver
from selenium.webdriver.common.by import By
Ch_opt = webdriver.ChromeOptions()
Ch_opt.add_argument("--start-maximized")
Ch_opt.add_argument("headless")
Ch_opt.add_argument("--ignore-certificate")
driver = webdriver.Chrome(options=Ch_opt)
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#driver.maximize_window()
print(driver.title)