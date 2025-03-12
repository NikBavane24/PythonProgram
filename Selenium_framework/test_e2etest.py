import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()  # for CSS a[href*='shop']
    phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for i in phones:
        phone_name = i.find_element(By.XPATH, "div/h4/a").text
        if phone_name == "Samsung Note 8":
            i.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("Ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
    driver.find_element(By.LINK_TEXT, 'India').click()
    driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
    driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
    Msg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert']").text

    assert "Success! Thank you!" in Msg

    time.sleep(5)
