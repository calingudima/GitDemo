

from time import sleep

import driver as driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://trade.thinkorswim.com")
driver.implicitly_wait(15)

print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, "username0").send_keys("workcartel")
driver.find_element(By.ID, "password1").send_keys("Charlotte2022")
driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
driver.find_element(By.ID, "accept").click()
driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("AAPL")

driver.find_element(By.XPATH, "//span[normalize-space()='APPLE INC COM']").click()

driver.find_element(By.XPATH, "//button[@direction='buy']").click()
driver.find_element(By.XPATH, "//input[@type='number']").click()


for i in range(3):
    driver.find_element(By.XPATH, "//input[@type='number']").send_keys(Keys.BACK_SPACE)

driver.find_element(By.XPATH, "//input[@type='number']").send_keys(15)

driver.find_element(By.CSS_SELECTOR, "#review-order-button").click()
driver.find_element(By.CSS_SELECTOR, "#send-order-button").click()

driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click()

original_confirmation = []

original_message = [driver.find_element(By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]").text]
print(original_message)

for records in original_message:
    original_confirmation.append(records)
print(original_confirmation)
assert original_message == original_confirmation



sleep(10)
driver.quit()





