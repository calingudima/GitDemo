from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://shopping.beeyor.com/shop/")
sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
sleep(2)
select = Select(driver.find_element(By.XPATH, "(//select[@class='orderby'])[1]"))
select.select_by_index(3)

sleep(2)

driver.quit()