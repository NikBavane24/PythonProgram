import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v128.fed_cm import click_dialog_button
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()  #Hoveroer
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()    #Right Click
action.click(driver.find_element(By.LINK_TEXT,"Reload")).perform()
time.sleep(2)
#action.double_click()  Double click_dialog_button()
#action.drag_and_drop()  Drag and drop element
#action.click()  click an element
#action.click_and_hold() click and hold