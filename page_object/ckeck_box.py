import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://grotechminds.com/is-selected/")
    check_box = driver.find_element(By.XPATH,"(//input[@id='vehicle2'])[3]")
    check_box.click()
    if check_box.is_selected():
        assert True
    else:
        assert False
    time.sleep(5)
except Exception as e:
    print(e)
