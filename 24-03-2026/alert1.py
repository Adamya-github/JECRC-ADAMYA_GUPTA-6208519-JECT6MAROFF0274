from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(3)

## switching to alert using wait
wait = WebDriverWait(driver,10)
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.accept()
sleep(3)
