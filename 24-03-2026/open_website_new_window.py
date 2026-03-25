from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(3)

## this open new website in same tab
driver.get('https://www.google.com/')
sleep(3)

## Opening a website in new tab
driver.switch_to.new_window('tab')
driver.get('https://www.google.com/')
sleep(3)

## Opening a website in new window
driver.switch_to.new_window('window')
driver.get('https://www.google.com/')
sleep(3)


## Opening a website in new tab
driver.switch_to.new_window('tab')
driver.get('https://www.google.com/')
sleep(3)