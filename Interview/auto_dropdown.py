import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.skyscanner.co.in/?&utm_source=google&utm_medium=cpc&utm_campaign=IN-Flights-Search-EN-Generics-New&utm_term=flight+booking&associateID=SEM_FLI_19465_00000&campaign_id=19347634260&adgroupid=147703716634&keyword_id=kwd-18709060&gad_source=1&gad_campaignid=19347634260&gbraid=0AAAAAD3oWFhwHtETIqzEIeCQBbwb5iXXD&gclid=EAIaIQobChMI64LTu47KjQMVaN0WBR3a_ClHEAAYAiAAEgL1ZfD_BwE&gclsrc=aw.ds")
driver.find_element(By.XPATH,"(//input[@placeholder='Country, city or airport'])[1]").clear()
driver.find_element(By.XPATH,"(//input[@placeholder='Country, city or airport'])[1]").send_keys("Pune")
dropdown_atm=driver.find_element(By.XPATH,"(//input[@placeholder='Country, city or airport'])[1]").get_attribute("value")

for i in dropdown_atm:
    print(i)
    if i.find_element(By.XPATH,"//div[@class='wM6W7d']/span")=="kolhapur mahalaxmi":
        i.click()
time.sleep(5)