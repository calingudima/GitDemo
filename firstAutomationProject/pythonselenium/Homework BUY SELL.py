from time import sleep

import driver as driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)



#driver.maximize_window()   # will maximize the window
# driver.minimize_window() # minimize

driver.get("https://trade.thinkorswim.com")

#driver.implicitly_wait(15)

# Synchronisations or WAITS
# 2 types of wait's - implicit and explicit wait
# they are designed to wait until the element is present on the page.

print(driver.title)
print(driver.current_url)

sleep(2)

driver.find_element(By.ID, "username0").send_keys("workcartel")
sleep(1)
driver.find_element(By.ID, "password1").send_keys("Charlotte2022")
sleep(1)
driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
sleep(1)
driver.find_element(By.ID, "accept").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("AAPL")
sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='APPLE INC COM']").click()
sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Buy']").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[data-testid='trade-quantity-input']").send_keys(Keys.BACK_SPACE * 3)
sleep(2)
driver.find_element(By. CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys("1")
sleep(2)
driver.find_element(By. ID, "review-order-button").click()
sleep(2)
driver.find_element(By. ID, "send-order-button").click()
sleep(4)