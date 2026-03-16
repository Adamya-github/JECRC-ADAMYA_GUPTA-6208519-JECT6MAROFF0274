from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

## Toggle between male and female
# l1 = ['male','female']
# for i in range(5):
#     for j in l1:
#         driver.find_element(By.ID,j).click() ## handle radio button
#         sleep(2)

## checkbox every checkbox and print its inner value and then uncheck backwards
l2 = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for j in l2:
    driver.find_element(By.XPATH, f'//label[text()="{j}"]/preceding-sibling::input').click()
    print(driver.find_element(By.XPATH,f'//label[text()="{j}"]').text)
    sleep(2)
for j in l2[::-1]:
    driver.find_element(By.XPATH, f'//label[text()="{j}"]/preceding-sibling::input').click()
    print(driver.find_element(By.XPATH, f'//label[text()="{j}"]').text)
    sleep(2)
driver.quit()