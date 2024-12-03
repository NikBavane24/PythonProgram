import time
from idlelib.editor import keynames

from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.poolmanager import key_fn_by_scheme

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.ID,"input").send_keys("India")

time.sleep(4)