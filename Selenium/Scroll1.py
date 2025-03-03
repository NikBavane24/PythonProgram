import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://grotechminds.com/vertical-scrolling/")
driver.implicitly_wait(5)

driver.execute_script("window.scroll(0,1800);")
time.sleep(2)
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
time.sleep(2)