from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#driver.maximize_window()
driver.get("https://trade.thinkorswim.com")
sleep(1)

driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
window = driver.window_handles
driver.switch_to.window(window[1])
sleep(2)
driver.close()
driver.switch_to.window(window[0])

driver.find_element(By.NAME, "su_username").send_keys("somedemo")

print(driver.current_url)
sleep(4)

driver.quit()
