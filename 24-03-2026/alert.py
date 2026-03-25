from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(3)

## simple alert
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
sleep(5)

## confirmation alert
driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
sleep(2)

driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.dismiss()
sleep(5)

## prompt alert
driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys('qwerty')
alert.accept()
sleep(5)

driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys('qwerty')
sleep(2)
alert.dismiss()
sleep(2)


