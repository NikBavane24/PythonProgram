import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Initialize WebDriver (using Firefox in this case)
driver = webdriver.Firefox()

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# Search for items
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

actualList = []
results = driver.find_elements(By.XPATH, "//div[@class='product']")

# Assert that there are results found
count1 = len(results)
assert count1 > 0

for result in results:
    actualList.append(result.text)

    # Wait for the product to be clickable and then click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='product']"))
    )
    try:
        result.click()
    except Exception as e:
        # If click still fails, scroll to the element and use JavaScript to click
        driver.execute_script("arguments[0].scrollIntoView(true);", result)
        driver.execute_script("arguments[0].click();", result)

print(actualList)

# Proceed to cart and checkout
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(2)

# Calculate the total price
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
Sum = sum(int(price.text) for price in prices)
print(Sum)

total = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

# Assert that the calculated total matches the displayed total
assert Sum == total

# Apply promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Wait for promo code confirmation message
wait = WebDriverWait(driver, 10)
promo_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo"))
)
print(promo_message.text)

time.sleep(2)

# Validate that expected and actual lists match
expectedList = ['Cucumber - 1Kg', 'Rasberry -1/4 Kg', 'Strawberry - 1/4 Kg']
assert expectedList == actualList

# Close the driver after execution
driver.quit()
