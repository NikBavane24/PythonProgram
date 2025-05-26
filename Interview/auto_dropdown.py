import time

from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)