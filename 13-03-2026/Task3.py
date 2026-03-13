from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()

sleep(2)

print("Amazon opened successfully")

# 1. Locate main search bar using ID with CSS Selector
search_bar = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print(search_bar)
print("Search bar found")

# 2. Locate Amazon logo using CSS selector
logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")
print(logo)
print("Amazon logo found")

# 3. Locate Cart icon using CSS selector
cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print(cart)
print("Cart icon found")

# 4. Locate Sign in link using descendant selector
signin = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")
print(signin)
print("Sign in link found")

# 5. Locate all category links under navigation bar

categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")

print(categories)
print(len(categories))
print("Total navigation category links found")

sleep(3)

driver.quit()
