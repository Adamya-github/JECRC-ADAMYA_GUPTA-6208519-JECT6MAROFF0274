## is_displayed, is_enabled, is_selected --> it shows the boolean values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

male = driver.find_element(By.ID,'male')
male.click()
print(male.is_displayed())
print(male.is_enabled())

check = driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
check.click()
print(check.is_selected())

sleep(2)

driver.quit()

## if ui or DOM structure is not loaded together, that is some time ui load faster than DOM or DOM loads
# faster then ui, then it will create a problem for identification, so we use wait