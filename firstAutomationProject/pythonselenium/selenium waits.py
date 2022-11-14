from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/")
sleep(2)
driver.find_element(By.XPATH, "//a[text()='Dynamic Controls']").click()
sleep(1)
driver.find_element(By.XPATH, "(//button[@type='button'])[2]").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Disable']")))
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("dfhg")
sleep(1)
print(driver.find_element(By.CSS_SELECTOR, "p[id='message']").text)

driver.quit()