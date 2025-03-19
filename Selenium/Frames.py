import time


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Text frames")
time.sleep(5)