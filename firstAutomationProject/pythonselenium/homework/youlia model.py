
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# amount = 15
# discount = amount * 0.10
# total_amount_after_discount = amount - discount

# homework - confirm and make sure that the discount is 10%.
# Then make sure that after the discount you pay the price displayed.


service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(15)
driver.get("http://shopping.beeyor.com/shop/")
# sleep(2)
list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
for item in list_of_items:
    item.click()
    if item == driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[2]"):
        break

sleep(2)
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='cart-contents']")).perform()
sleep(1)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward']")).click().perform()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='coupon_code']").send_keys("Tojtech Automation")
sleep(2)
driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
print(driver.find_element(By.XPATH, "//div[@role='alert']").text)
sleep(2)
driver.execute_script("window.scrollBy(0,500)", "")

total_amount = driver.find_element(By. XPATH, "//a[@title='View your shopping cart']//span[@class='woocommerce-Price-amount amount']").text
print(total_amount)

a = total_amount[1:6]
print(a)
a1 = float(a)
print("Total amount before coupon: $", a1)
discount = round((a1 * 0.10), 2)
print("10% coupon should be:$", discount)
sleep(2)
discount_amount = driver.find_element(By.XPATH, "//tr[@class='cart-subtotal']//bdi[1]").text
b = discount_amount[1:8]
b1 = float(b)
print("Coupon amount applied:$", b1)
sleep(2)
if discount == b1:
    print("Congrats! 10% discount has been successfully applied to your order")
else:
    print("Sorry! Discount amount was not applied properly")

Total_amount_after_discount = (a1 - b1)
print("Total_amount_after_discount:$", Total_amount_after_discount)
sleep(3)
driver.quit()
