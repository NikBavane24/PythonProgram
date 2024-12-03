import time

from selenium import webdriver
from selenium.webdriver.common.by import By

a = webdriver.ChromeOptions()
a.add_argument('headless')

driver = webdriver.Chrome(options=a)
#driver = webdriver.Firefox()
#driver = webdriver.Edge()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scroll(0,500);")
#driver.execute_script("window.scroll(0,document.body.scrollHeight);")
time.sleep(2)
driver.get_screenshot_as_file("Screen.png")