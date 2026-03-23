from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get(r'C:\Users\Adamya Gupta\OneDrive\Desktop\Testing_Tech\JECRC\23-03-2026\index.html')
driver.maximize_window()
action = ActionChains(driver)

present = driver.find_element(By.ID, 'presentAddress')
present.send_keys('JECRC, Jaipur, Raj')
permanent = driver.find_element(By.ID,'permanentAddress')
sleep(2)

present.click()
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(1)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
sleep(2)

permanent.click()
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(2)
