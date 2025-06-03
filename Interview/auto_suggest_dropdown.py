import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
opt=webdriver.ChromeOptions()
opt.add_argument("headless")
opt.add_argument("--start-maximized")
driver= webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
wait= WebDriverWait(driver,10)
wait.until(lambda driver:driver.find_element(By.XPATH,"//li[@class='ui-menu-item']"))
Dropdown_atoms=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for Dropdown_atom in Dropdown_atoms:
    print(Dropdown_atom.text)
    if Dropdown_atom.text=="Indonesia":
        Dropdown_atom.click()
        break
time.sleep(5)
driver.close()