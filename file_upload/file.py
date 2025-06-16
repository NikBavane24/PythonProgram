import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from file_upload.config import url, file_path

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)
driver.find_element(By.CSS_SELECTOR,"input[name='userfile']").send_keys(file_path)
time.sleep(10)