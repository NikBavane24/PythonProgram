import time
from typing import KeysView

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"(//button[@type='button'])[16]").click()
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.XPATH,"//body[@id='tinymce']").send_keys(Keys.BACK_SPACE)
driver.find_element(By.XPATH,"//body[@id='tinymce']").send_keys("Text frames")
time.sleep(5)
driver.switch_to.default_content()