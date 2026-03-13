from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = opts)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

sleep(2)

print("Website opened successfully")

# 1. Locate username field using XPath with tag and name attribute
username = driver.find_element(By.XPATH, '//input[@name="username"]')
print(username)
print("Username field found")

# 2. Locate password field using XPath with tag and id attribute
password = driver.find_element(By.XPATH, '//input[@id="password"]')
print(password)
print("Password field found")

# 3. Locate login button using XPath with tag and type attribute
login_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
print(login_btn)
print("Login button found")

# 4. Locate Elemental Selenium link using exact text
elemental_link = driver.find_element(By.XPATH, '//a[text()="Elemental Selenium"]')
print(elemental_link)
print("Elemental Selenium link found")

# 5. Locate main heading Login Page using contains() with text
heading = driver.find_element(By.XPATH, '//h2[contains(text(),"Login")]')
print(heading)
print("Login Page heading found")

sleep(3)

driver.quit()
