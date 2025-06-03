import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://grotechminds.com/multiple-select/")
driver.find_element(By.CSS_SELECTOR,"span[class='select2-selection select2-selection--multiple']").click()
dropdown_atoms = driver.find_elements(By.XPATH,"//li[@role='treeitem']")
for dropdown_atom in dropdown_atoms:
    if dropdown_atom.text=="Motorcycle":
        dropdown_atom.click()
        break
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "span[class='select2-selection select2-selection--multiple']").click()
dropdown_atoms = driver.find_elements(By.XPATH,"//li[@role='treeitem']")
for dropdown_atom in dropdown_atoms:
    if dropdown_atom.text=="Sedan":
        dropdown_atom.click()
        time.sleep(5)