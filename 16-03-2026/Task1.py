from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print("Page Title:", driver.title)
sleep(2)

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()

sleep(3)

url = driver.current_url
print("Current URL:", url)


if "dashboard" in url:
    print("Successful Login")


driver.quit()
