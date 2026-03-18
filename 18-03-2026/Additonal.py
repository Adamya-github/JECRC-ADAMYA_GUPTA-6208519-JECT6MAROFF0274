from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/lenskart-blu-lb-e14789-c1-eyeglasses.html')
driver.maximize_window()
sleep(5)

but1 = driver.find_element(By.XPATH,'//div[@class="sc-39b66eee-3 eEeoNR"]/h4')
but1.click()
sleep(2)
check = driver.find_element(By.XPATH, '//div[@class="sc-a3b31f26-14 fDEfLM"]')
print(check.is_enabled())

driver.quit()

## Pausing