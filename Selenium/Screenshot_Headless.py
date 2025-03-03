import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_argument("headless")
#opt.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=opt)
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)


driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen1.png")
time.sleep(2)