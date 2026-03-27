from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title)
print(driver.current_url)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Headphones",Keys.RETURN)
sleep(2)

driver.find_element(By.XPATH,'(//div[@class="a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left"])[4]').click()
sleep(2)

min_price = driver.find_element(By.XPATH, "//input[@aria-label='Minimum price']")
max_price = driver.find_element(By.XPATH, "//input[@aria-label='Maximum price']")
min_price.send_keys("1000")
max_price.send_keys("2000")
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
sleep(3)

first_product = driver.find_element(By.XPATH, "(//h2/a)[1]")
product_name = first_product.text
first_product.click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

product_title = driver.find_element(By.ID, "productTitle").text
assert product_name[:10] in product_title, "Product title mismatch"

product_price = driver.find_element(By.XPATH, "//span[@class='a-price-whole']").text
assert product_price != "", "Price not displayed"

driver.find_element(By.ID, "add-to-cart-button").click()
sleep(2)

driver.find_element(By.ID, "nav-cart").click()

cart_product = driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
assert product_name[:10] in cart_product, "Cart item mismatch"
print("Test Completed Successfully ")


driver.quit()