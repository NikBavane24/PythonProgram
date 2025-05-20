import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#river = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID,'downloadButton').click()


file_upload=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_path="D:\\download.xlsx"
file_upload.send_keys(file_path)

locator=(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2")
WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(locator))
print(driver.find_element(*locator).text)
time.sleep(5)