

# each part ICON on the page has its own location, we right click and inspect the ICON and see where it is located. DEV TOOLS.
#     What is the best locator from listed?
#     ID locator in Selenium is the most preferred and fastest way to locate desired WebElenInts
#     on the page. ID Selenium locators are unique for each element in the DOM. Since IDs are
#     unique for each element on the page, it is considered the fastest and safest method to
#     locate elements. Nov 15, 2021

# Locator - the adress of each particular element on the webpage based on which we can acces the element directly.

# locator types :
#                Static - comes by default:  ID, Name, Class name, Link, Parcial link, text, tag.
#                        complex locators : XPATH and CSS selector.
#
# EVERY SINGLE PAGE IS EVERY SINGLE FILE AND CLASS IN PYTHON

# to perform operations in our browser we use <<<DRIVER.blablabla>>>

# for <<<clases>>> we use DOT ( . ) in the web browser in devtools
# for <<<ID>>> we use HASH ( # ) sign in the devtools.

# CSS SELECTOR --- input[id='navigation-symbol-search']
# We use SLEEP function in order to give the website some time to load all the information and then to paste our code.


from time import sleep


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)


driver.get("http://trade.thinkorswim.com/")

driver.find_element(By.ID, "username0").send_keys("workcartel")

# ID, Name, CLASS_NAME,
# XPATH - //tag_name[@attribute_name='value'] ->

# CSS - tag_name[attribute_name='value']
# BY.ID
# By.CSS_SELECTOR = #username0 -> input[id='username0']
# for class we use dot


sleep(2)
driver.find_element(By.ID, "password1").send_keys("Charlotte2022")
sleep(2)
driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()   # we created a unique ID  with @  PATH
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()  # We use a partial link
sleep(2)
driver.quit()
# driver.find_element(By.CLASS_NAME, "accept").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("TW")
# sleep(4)
# CSS SELECTOR syntax --- input[id='navigation-symbol-search']
# XPATH selector --- //label[@for='rememberuserid']
#driver.quit()


# //p[text()='This is a paperMoney account.']  Can work if only it is not a hyper link

# div for graphical design
# button - tag name button
# input field - input tag


# ABSOLUT XPATH and RELATIVE XPATH
#
# Absolut xpath - going from top of the line and goind down till bottom
# scans the entire downtree page and will include all the elements in your XPATH text, from top to bottom.
#
# //div[@class='row calltoaction']/input[2]    DASHA SASHA example
#
# find the diference between absolut and relative
#


# what better to use ?  XPATH OR CSS ?
#
#
#
#





