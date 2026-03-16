## today's methods: send_keys(), clear(), get_attribute(), Keys.ENTER
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in')
driver.maximize_window()

sleep(2) ## why using this below is working and without it is it not working-->s

search = driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon.in"]')
search.clear()
search.send_keys('LPG Cylinder')
print(search.get_attribute('placeholder'))
print(search.get_attribute('value'))
search_it = driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
search_it.click()
sleep(2)

search1 = driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon.in"]')
search1.clear()
search1.send_keys('LPG Cylinder for hotel', Keys.ENTER)

search2 = driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon.in"]')
search2.clear()
sleep(2)
driver.quit()