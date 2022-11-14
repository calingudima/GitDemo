from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/usr/local/bin/chromedriver")   # this service is a class, we need to import it by hovering over it.
driver = webdriver.Chrome(service=service_obj)  # service is a property that is responsible for location of chrome driver

# the ,,driver,, object has access to all the properties in our chrome class.

driver.get("https://trade.thinkorswim.com/")
print(driver.title) # we get the title in console
print(driver.current_url) # show on what web address we are
sleep(2)   # Freezing the time for holding the page open in seconds timing
driver.get("https://apple.com/") # will go to the URL ( website ) provided.
sleep(2)
driver.back() # takes us one page back in our browser.
sleep(2)
driver.forward() # takes us to the next page
sleep(2)
driver.refresh() # refreshing our page
driver.close() # just the tab close
# driver.quit() # close the chrome browser

# each part ICON on the page has its own location, we right click and inspect the ICON and see where it is located. DEV TOOLS. 



































