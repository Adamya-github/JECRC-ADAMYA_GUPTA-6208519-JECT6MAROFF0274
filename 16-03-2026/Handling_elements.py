from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

name = driver.find_element(By.ID, 'name') ## locator, locator expression
name.clear()
name.send_keys('Adamya')
sleep(2)

email = driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
email.send_keys('ada@1.con')
sleep(2)
# print(name.get_attribute('placeholder')) ## this method sends the value that is stored in it
# print(name.get_attribute('value')) ## despite of not having value attribute , it shows that which value is written in it

driver.find_element(By.ID,'male').click() ## handle radio button
sleep(2)

driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
sleep(2)

# monday_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
# print(monday_checkbox.text) ## here and below .text is used to get inner element text, it will not return the attribute text
print(driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label').text)
sleep(2)

driver.quit()