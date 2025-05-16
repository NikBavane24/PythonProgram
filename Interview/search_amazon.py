import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#driver=webdriver.Chrome()
driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5km84u9k2k_e&adgrpid=155259813113&hvpone=&hvptwo=&hvadid=674842289479&hvpos=&hvnetw=g&hvrand=3174765027840429831&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9301198&hvtargid=kwd-304880464215&hydadcr=14450_2316420&gad_source=1")
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Toys")
driver.find_element(By.ID,"twotabsearchtextbox").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()