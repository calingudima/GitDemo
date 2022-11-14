# thu oct 13

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument("--start-maximized")
# options.add_argument("--kiosk")
#options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
#
# service_obj = Service("/usr/local/bin/chromedriver")
# driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://class.beeyor.com/")
driver.minimize_window()
sleep(2)

driver.find_element(By.ID, "username").send_keys("fdfdfd")


#driver.quit()

# use headles mode to buy and sell in


# homework
# go back of thinkorswim to find out if the driver closes or not
# child window, impliment the headles mode, verify if the driver closes after the
# execution is done or not.
