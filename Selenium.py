import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Demobrowser import service
class test_chromelaunch:
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")


#service_o = Service("C:\Users\nikhil.bavane\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#driver = webdriver.chrome(service=service_o)

#driver = webdriver.Chrome()

#time.sleep(3)
