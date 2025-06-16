

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



options = Options()
options.add_experimental_option("detach", True)
def method(username,password):
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.ID,"pass").send_keys(password)

method("testmiq.qa@ces-ltd.com","Test@1234")
