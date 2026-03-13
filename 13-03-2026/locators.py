from selenium import webdriver     # Used to control the browser
from time import sleep             # Used to pause execution for some time
# Selenium provides different ways to locate elements
from selenium.webdriver.common.by import By

# HOW TO INSPECT ELEMENTS IN A WEBPAGE
# Three ways to open the browser inspector:
# 1. Right click on the element → Click "Inspect", # 2. Press Ctrl + Shift + I, # 3. Press F12

# find_element()
# Returns the FIRST matching element, # If element not found → throws an error

# find_elements()
# Returns a LIST of all matching elements, # If element not found → returns empty list

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)
print('Browser started successfully')

# Old / incorrect usage
# driver.find_element('id'), # This is not efficient and not recommended in modern Selenium

# Recommended method: Use By class to clearly specify the locator strategy

# Why copy ID or class directly from inspect?
# Prevents typing mistakes, Avoids extra spaces or wrong characters, Ensures locator accuracy

name = driver.find_element(By.ID, 'name')
phone = driver.find_element(By.ID,'phone')
# nav_bar = driver.find_element(By.ID,'navbar')
nav_bar = driver.find_element(By.NAME,'Navbar')
# radio_button = driver.find_element(By.CLASS_NAME,'form-check-label')
radio_button = driver.find_elements(By.CLASS_NAME,'form-check-label') ## to consider all elements, if no element found then it will return empty list [] with len 0
inp = driver.find_elements(By.TAG_NAME, 'input')

print(name)
print('name textfield Found')
print(phone)
print("phone textfield found")
print(nav_bar)
print("nav_bar found")
print(radio_button)
print(len(radio_button))
print('Radio button found')
print(inp)
print(len(inp))
print('input Tag found')



