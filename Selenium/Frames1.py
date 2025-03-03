import time


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://grotechminds.com/add-to-cart/")
driver.implicitly_wait(5)
driver.switch_to.frame("frame")
driver.find_element(By.ID,"firstName").send_keys("XYZ")
driver.find_element(By.ID,"lastName").send_keys("Text frames")
time.sleep(5)